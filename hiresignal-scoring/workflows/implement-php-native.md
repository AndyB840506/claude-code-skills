# Workflow: Implement PHP Native Scoring Engine (No Engineer Needed)

**Goal:** Build a single PHP file that companies drop into their website. Upload JD, process transcripts, get reports. Zero engineering knowledge required.

**Duration:** 1 week  
**Owner:** (Anyone can deploy - it's just a PHP file)  
**Output:** `hiresignal-scoring.php` - Single file, self-contained, zero config

---

## Vision

**For the client:**
1. Upload JD via web form
2. Upload interview transcript (text)
3. Click "Score"
4. Get HTML report to download/print
5. Done.

**No servers to manage. No databases. No deployment. Just a PHP file.**

---

## Step 0: Architecture

```
┌─────────────────────────────────────┐
│    Client's Website / Server         │
│  (Any hosting with PHP support)      │
│                                      │
│  ┌──────────────────────────────┐   │
│  │  hiresignal-scoring.php      │   │
│  │  (Single 500KB file)         │   │
│  │                              │   │
│  │  ├─ Web UI (upload JD)       │   │
│  │  ├─ Web UI (upload transcript)   │
│  │  ├─ Claude API integration   │   │
│  │  ├─ Scoring logic            │   │
│  │  ├─ HTML report generation   │   │
│  │  └─ Download as PDF          │   │
│  └──────────────────────────────┘   │
│                 │                    │
│        (uses client's DB or         │
│         session storage)            │
└────────────────┼────────────────────┘
                 │
                 ▼
        ┌─────────────────┐
        │  Claude API     │
        │  (Analysis)     │
        └─────────────────┘
```

---

## Step 1: Setup & Dependencies

**What the client needs:**
- PHP 7.4+ (standard on most hosts)
- `curl` extension (enabled by default)
- A Claude API key (they provide in settings form)
- 1 MB disk space

**That's it. No npm, no composer, no build tools.**

---

## Step 2: Build hiresignal-scoring.php

### Core Structure

```php
<?php
/**
 * HireSignal Scoring Engine - PHP Native
 * Version: 1.0
 * 
 * Simple drop-in scoring solution using Claude API
 * No engineers needed. Just upload and use.
 */

error_reporting(E_ALL);
ini_set('display_errors', 0);
ini_set('log_errors', 1);

session_start();

// ============================================
// CONFIGURATION
// ============================================

const CLAUDE_API_URL = "https://api.anthropic.com/v1/messages";
const CLAUDE_MODEL = "claude-opus-4-7";

// Settings stored in session/file
$settings = [
    'claude_api_key' => $_SESSION['claude_api_key'] ?? '',
    'company_name' => $_SESSION['company_name'] ?? '',
];

// ============================================
// ROUTING
// ============================================

$action = $_GET['action'] ?? 'index';

switch ($action) {
    case 'settings':
        handleSettings();
        break;
    case 'score':
        handleScore();
        break;
    case 'report':
        handleReport();
        break;
    default:
        showHome();
        break;
}

// ============================================
// PAGE: Home / Upload
// ============================================

function showHome() {
    ?><!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>HireSignal Scoring Engine</title>
    <style>
        /* Visual design: choose colors and style that fit the project's brand.
           Do NOT copy these exact values — adapt to the client's palette. */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, sans-serif;
            background: var(--brand-gradient, linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%));
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            max-width: 600px;
            width: 100%;
            padding: 40px;
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 28px;
        }
        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 14px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 500;
            font-size: 14px;
        }
        input[type="text"],
        input[type="password"],
        textarea,
        select {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-family: inherit;
            font-size: 14px;
        }
        textarea {
            min-height: 150px;
            resize: vertical;
            font-family: 'Courier New', monospace;
        }
        button {
            width: 100%;
            padding: 12px;
            background: var(--brand-gradient, linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%));
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
        }
        button:hover {
            transform: translateY(-2px);
        }
        .settings-link {
            text-align: center;
            margin-top: 20px;
        }
        a {
            color: #4f46e5;
            text-decoration: none;
            font-size: 14px;
        }
        a:hover {
            text-decoration: underline;
        }
        .error {
            background: #fee;
            color: #c33;
            padding: 12px;
            border-radius: 5px;
            margin-bottom: 20px;
            font-size: 14px;
        }
        .success {
            background: #efe;
            color: #3c3;
            padding: 12px;
            border-radius: 5px;
            margin-bottom: 20px;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 HireSignal</h1>
        <p class="subtitle">Interview Scoring Engine</p>

        <?php
        $api_key = $_SESSION['claude_api_key'] ?? '';
        if (!$api_key) {
            echo '<div class="error">⚠️ API key not configured. <a href="?action=settings">Configure settings</a></div>';
        }
        ?>

        <form method="POST" action="?action=score">
            <div class="form-group">
                <label>Job Title *</label>
                <input type="text" name="job_title" placeholder="e.g., Senior Backend Engineer" required>
            </div>

            <div class="form-group">
                <label>Role Level *</label>
                <select name="role_level" required>
                    <option value="">-- Select --</option>
                    <option value="junior">Junior (6.0 threshold)</option>
                    <option value="mid">Mid-Level (6.5 threshold)</option>
                    <option value="senior">Senior (7.0 threshold)</option>
                    <option value="leadership">Leadership (7.5 threshold)</option>
                </select>
            </div>

            <div class="form-group">
                <label>Interview Transcript *</label>
                <textarea name="transcript" placeholder="Paste the full interview transcript here..." required></textarea>
            </div>

            <div class="form-group">
                <label>Culture Type (optional)</label>
                <select name="culture">
                    <option value="">-- Select --</option>
                    <option value="startup">Startup (bias for action)</option>
                    <option value="corporate">Corporate (process-oriented)</option>
                    <option value="remote">Remote-first (communication)</option>
                    <option value="leadership">Leadership-focused</option>
                    <option value="collaborative">Collaborative</option>
                </select>
            </div>

            <button type="submit">📊 Score Interview</button>
        </form>

        <div class="settings-link">
            <a href="?action=settings">⚙️ Configure API Key</a>
        </div>
    </div>
</body>
</html>
    <?php
}

// ============================================
// PAGE: Settings
// ============================================

function handleSettings() {
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $_SESSION['claude_api_key'] = $_POST['api_key'] ?? '';
        $_SESSION['company_name'] = $_POST['company_name'] ?? '';
        $message = '✅ Settings saved!';
    }

    $api_key = $_SESSION['claude_api_key'] ?? '';
    $company_name = $_SESSION['company_name'] ?? '';
    ?><!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Settings - HireSignal</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            max-width: 600px;
            width: 100%;
            padding: 40px;
        }
        h1 { color: #333; margin-bottom: 30px; }
        .form-group { margin-bottom: 20px; }
        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 500;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 14px;
        }
        button {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 5px;
            font-weight: 600;
            cursor: pointer;
        }
        .back-link {
            margin-top: 20px;
            text-align: center;
        }
        a {
            color: #667eea;
            text-decoration: none;
        }
        .success {
            background: #efe;
            color: #3c3;
            padding: 12px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚙️ Settings</h1>

        <?php if (isset($message)) echo "<div class='success'>$message</div>"; ?>

        <form method="POST">
            <div class="form-group">
                <label>Claude API Key *</label>
                <input type="password" name="api_key" value="<?php echo htmlspecialchars($api_key); ?>" required>
                <small>Get your API key from <a href="https://console.anthropic.com" target="_blank">console.anthropic.com</a></small>
            </div>

            <div class="form-group">
                <label>Company Name (optional)</label>
                <input type="text" name="company_name" value="<?php echo htmlspecialchars($company_name); ?>" placeholder="e.g., Kuma Talent">
            </div>

            <button type="submit">💾 Save Settings</button>
        </form>

        <div class="back-link">
            <a href="?action=index">← Back to Home</a>
        </div>
    </div>
</body>
</html>
    <?php
}

// ============================================
// ACTION: Score Interview
// ============================================

function handleScore() {
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        header('Location: ?action=index');
        exit;
    }

    $api_key = $_SESSION['claude_api_key'] ?? '';
    if (!$api_key) {
        die('Error: API key not configured');
    }

    $job_title = $_POST['job_title'] ?? '';
    $role_level = $_POST['role_level'] ?? 'mid';
    $transcript = $_POST['transcript'] ?? '';
    $culture = $_POST['culture'] ?? '';

    // Call Claude API to score
    $scoring_result = callClaudeScoring($api_key, $transcript, $role_level, $culture, $job_title);

    // Save to session (or file for persistence)
    $_SESSION['last_score'] = $scoring_result;
    $_SESSION['job_title'] = $job_title;
    $_SESSION['role_level'] = $role_level;

    // Redirect to report
    header('Location: ?action=report');
    exit;
}

// ============================================
// ACTION: Generate & Show Report
// ============================================

function handleReport() {
    $score = $_SESSION['last_score'] ?? null;
    $job_title = $_SESSION['job_title'] ?? 'Unknown';

    if (!$score) {
        header('Location: ?action=index');
        exit;
    }

    // Render HTML report
    renderHTMLReport($score, $job_title);
}

// ============================================
// CLAUDE API INTEGRATION
// ============================================

function callClaudeScoring($api_key, $transcript, $role_level, $culture, $job_title) {
    // Threshold based on role
    $thresholds = [
        'junior' => 6.0,
        'mid' => 6.5,
        'senior' => 7.0,
        'leadership' => 7.5,
    ];
    $threshold = $thresholds[$role_level] ?? 6.5;

    // Load scoring schema
    $schema = json_decode(file_get_contents(__DIR__ . '/../../config/scoring-schema.json'), true);

    $prompt = <<<PROMPT
You are an expert recruiter scoring interview transcripts using the HireSignal framework.

INTERVIEW TRANSCRIPT:
---
{$transcript}
---

JOB CONTEXT:
- Title: {$job_title}
- Role Level: {$role_level}
- Culture: {$culture}
- Scoring Threshold: {$threshold}/10

SCORING REQUIREMENTS:
- Technical Depth (20%): Problem-solving, architecture, debugging, production experience
- Authenticity (20%): Contradiction analysis, consistency, specificity
- English Proficiency (5%): Response time, vocabulary, grammar, comprehension
- Behavioral/Cultural Fit (5%): Ownership, initiative, adaptability
- Cognitive Flexibility (2%): Handles ambiguity, adapts approach
- Pressure Resilience (1%): Stress handling, composure
- Culture-Specific (7%): Role-specific culture alignment

CONTRADICTIONS:
Classify any contradictions as:
- CRITICAL: Core contradiction (dealbreaker) → NOT_FIT override
- WARNING: Significant inconsistency → Flag, affects score
- NOTE: Minor variation → Document only

OUTPUT REQUIRED:
Return ONLY valid JSON (no markdown, no explanation):
{
  "technical_depth": {
    "score": <0-10>,
    "evidence": [
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."},
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."},
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."}
    ],
    "reasoning": "..."
  },
  "authenticity": {
    "score": <0-10>,
    "contradictions": [
      {"type": "CRITICAL|WARNING|NOTE", "issue": "...", "evidence": "..."}
    ],
    "evidence": [
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."},
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."},
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."}
    ],
    "reasoning": "..."
  },
  "english_proficiency": {
    "score": <0-10>,
    "passes_threshold": true|false,
    "evidence": [
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."},
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."},
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."}
    ],
    "reasoning": "..."
  },
  "behavioral_fit": {
    "score": <0-10>,
    "culture_alignment": "{$culture}",
    "evidence": [
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."},
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."},
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."}
    ],
    "reasoning": "..."
  },
  "cognitive_flexibility": {
    "score": <0-10>,
    "evidence": [
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."},
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."},
      {"quote": "...", "context": "...", "confidence": 0.0-1.0, "reasoning": "..."}
    ],
    "reasoning": "..."
  },
  "verdict": "PASS|PASS_CONDITIONAL|REJECT",
  "overall_score": <0-10>,
  "confidence": <0-100>,
  "key_strengths": ["...", "...", "..."],
  "areas_of_concern": ["...", "...", "..."],
  "recommendation_summary": "..."
}
PROMPT;

    $ch = curl_init(CLAUDE_API_URL);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_HTTPHEADER => [
            'anthropic-version: 2023-06-01',
            'content-type: application/json',
            'x-api-key: ' . $api_key,
        ],
        CURLOPT_POSTFIELDS => json_encode([
            'model' => CLAUDE_MODEL,
            'max_tokens' => 4096,
            'messages' => [
                [
                    'role' => 'user',
                    'content' => $prompt,
                ]
            ]
        ]),
    ]);

    $response = curl_exec($ch);
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($http_code !== 200) {
        die("API Error ($http_code): " . htmlspecialchars($response));
    }

    $data = json_decode($response, true);
    $result_text = $data['content'][0]['text'] ?? '';

    // Parse JSON from response
    $scoring = json_decode($result_text, true);
    if (!$scoring) {
        die('Error parsing scoring result. Response: ' . htmlspecialchars($result_text));
    }

    return $scoring;
}

// ============================================
// REPORT GENERATION
// ============================================

function renderHTMLReport($score, $job_title) {
    $verdict = $score['verdict'] ?? 'UNKNOWN';
    $overall_score = $score['overall_score'] ?? 0;
    $confidence = $score['confidence'] ?? 0;

    // Color based on verdict
    $verdict_color = $verdict === 'PASS' ? '#28a745' : ($verdict === 'PASS_CONDITIONAL' ? '#ffc107' : '#dc3545');
    $verdict_label = $verdict === 'PASS' ? '✅ PASS' : ($verdict === 'PASS_CONDITIONAL' ? '⚠️ CONDITIONAL' : '❌ REJECT');

    ?><!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Assessment Report - <?php echo htmlspecialchars($job_title); ?></title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
            padding: 20px;
        }
        .report {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        .header h1 {
            font-size: 32px;
            margin-bottom: 10px;
        }
        .verdict-box {
            background: <?php echo $verdict_color; ?>;
            color: white;
            padding: 20px;
            border-radius: 5px;
            text-align: center;
            margin: 20px;
            font-size: 24px;
            font-weight: bold;
        }
        .score-display {
            text-align: center;
            padding: 20px;
        }
        .score-number {
            font-size: 48px;
            font-weight: bold;
            color: #667eea;
        }
        .score-label {
            color: #666;
            margin-top: 10px;
        }
        .content {
            padding: 40px;
        }
        .dimension {
            margin-bottom: 30px;
            border-left: 4px solid #667eea;
            padding-left: 20px;
        }
        .dimension-title {
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }
        .dimension-score {
            font-size: 14px;
            color: #666;
            margin-bottom: 15px;
        }
        .evidence {
            background: #f9f9f9;
            padding: 12px;
            border-radius: 5px;
            margin: 10px 0;
            border-left: 3px solid #667eea;
        }
        .quote {
            font-style: italic;
            color: #555;
            margin-bottom: 5px;
        }
        .context {
            font-size: 12px;
            color: #999;
        }
        .confidence {
            font-size: 11px;
            color: #999;
            margin-top: 5px;
        }
        .reasoning {
            color: #666;
            font-size: 14px;
            margin-top: 10px;
        }
        .footer {
            background: #f5f5f5;
            padding: 20px;
            text-align: center;
            color: #999;
            font-size: 12px;
        }
        .print-button {
            text-align: center;
            padding: 20px;
        }
        button {
            padding: 10px 20px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
        }
        button:hover {
            background: #764ba2;
        }
        @media print {
            .print-button { display: none; }
            body { background: white; padding: 0; }
        }
    </style>
</head>
<body>
    <div class="report">
        <div class="header">
            <h1>🎯 HireSignal Assessment Report</h1>
            <p>Interview Scoring Engine</p>
        </div>

        <div class="verdict-box">
            <?php echo $verdict_label; ?>
        </div>

        <div class="score-display">
            <div class="score-number"><?php echo number_format($overall_score, 1); ?>/10</div>
            <div class="score-label">Overall Score (Confidence: <?php echo $confidence; ?>%)</div>
        </div>

        <div class="content">
            <?php if (!empty($score['key_strengths'])): ?>
            <div class="dimension">
                <div class="dimension-title">✅ Key Strengths</div>
                <ul>
                    <?php foreach ($score['key_strengths'] as $strength): ?>
                    <li><?php echo htmlspecialchars($strength); ?></li>
                    <?php endforeach; ?>
                </ul>
            </div>
            <?php endif; ?>

            <?php if (!empty($score['areas_of_concern'])): ?>
            <div class="dimension">
                <div class="dimension-title">⚠️ Areas of Concern</div>
                <ul>
                    <?php foreach ($score['areas_of_concern'] as $concern): ?>
                    <li><?php echo htmlspecialchars($concern); ?></li>
                    <?php endforeach; ?>
                </ul>
            </div>
            <?php endif; ?>

            <?php
            // Render each dimension
            $dimensions = ['technical_depth', 'authenticity', 'english_proficiency', 'behavioral_fit', 'cognitive_flexibility'];
            $labels = [
                'technical_depth' => '🔧 Technical Depth',
                'authenticity' => '✓ Authenticity',
                'english_proficiency' => '🌍 English Proficiency',
                'behavioral_fit' => '👥 Behavioral/Cultural Fit',
                'cognitive_flexibility' => '🧠 Cognitive Flexibility',
            ];

            foreach ($dimensions as $dim):
                if (isset($score[$dim])):
                    $data = $score[$dim];
                    $dim_score = $data['score'] ?? 0;
            ?>
            <div class="dimension">
                <div class="dimension-title"><?php echo $labels[$dim]; ?></div>
                <div class="dimension-score">Score: <?php echo number_format($dim_score, 1); ?>/10</div>

                <?php if (!empty($data['evidence'])): ?>
                    <strong style="color: #666;">Evidence:</strong>
                    <?php foreach ($data['evidence'] as $evt): ?>
                    <div class="evidence">
                        <div class="quote">"<?php echo htmlspecialchars(substr($evt['quote'], 0, 150)); ?>..."</div>
                        <div class="context">Context: <?php echo htmlspecialchars($evt['context']); ?></div>
                        <div class="confidence">Confidence: <?php echo round($evt['confidence'] * 100); ?>%</div>
                    </div>
                    <?php endforeach; ?>
                <?php endif; ?>

                <?php if (!empty($data['reasoning'])): ?>
                <div class="reasoning"><strong>Analysis:</strong> <?php echo htmlspecialchars($data['reasoning']); ?></div>
                <?php endif; ?>
            </div>
            <?php
                endif;
            endforeach;
            ?>

            <?php if (!empty($score['recommendation_summary'])): ?>
            <div class="dimension">
                <div class="dimension-title">📋 Recommendation</div>
                <div class="reasoning"><?php echo htmlspecialchars($score['recommendation_summary']); ?></div>
            </div>
            <?php endif; ?>
        </div>

        <div class="print-button">
            <button onclick="window.print()">🖨️ Print / Download as PDF</button>
            <button onclick="window.location='?action=index'" style="margin-left: 10px;">← Score Another Interview</button>
        </div>

        <div class="footer">
            <p>Generated by HireSignal Scoring Engine | Internal Staff Only</p>
            <p>Report timestamp: <?php echo date('Y-m-d H:i:s'); ?></p>
        </div>
    </div>
</body>
</html>
    <?php
}
?>
