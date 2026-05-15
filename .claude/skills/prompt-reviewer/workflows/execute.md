# Prompt Reviewer Execution

Audit and improve prompts, skills, and instructions.

## Step 1: Choose Mode

**Default: QUICK MODE** (5 minutes)
- Review recently modified skills only
- Check for critical clarity issues
- Identify major gaps

**If user specified "thorough": THOROUGH MODE** (15 minutes)
- Review ALL skills in `.claude/skills/` comprehensively
- Check for syntax, consistency, and completeness
- Deep analysis of structure, patterns, and alignment
- Full effectiveness audit across entire skill library

## Step 2: Audit for Issues

Scan the skill files for:

**Clarity Issues:**
- Ambiguous language ("might", "sometimes", "could")
- Confusing structure (poor organization)
- Undefined terms or acronyms
- Contradictory statements
- Vague instructions

**Gaps:**
- Missing steps in workflows
- Undefined terms without examples
- No explanation of why something matters
- Missing edge case handling
- Incomplete decision trees

**Ineffectiveness:**
- Overly wordy explanations (should be concise)
- Missing context about when to use something
- Weak command/instruction clarity
- Poor examples or no examples at all
- Inconsistent formatting/style

**Pattern Violations:**
- Inconsistent naming (camelCase vs snake_case)
- Different documentation structure than other skills
- Breaking established conventions
- Tone mismatch with rest of project

## Step 3: Propose Improvements

For each issue found, provide:

**Problem:** File, line, issue, why it matters  
**Solution:** Specific before/after change

## Step 4: Ask Confirmation

Present findings and ask approval before applying changes.

## Step 5: Apply Changes (If Approved)

If approved: Update files and show confirmations  
If rejected: Discard changes
