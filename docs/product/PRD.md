# FlowWise — Product Requirements Document

## 1. Product Overview

FlowWise is an AI-enabled financial wellness platform designed to help
consumers better understand their cash flow, upcoming financial
obligations, spending patterns, and the potential impact of planned
purchases.

The product combines deterministic financial calculations with
generative AI explanations.

Core financial calculations remain outside the LLM to provide
predictable and auditable results.

---

## 2. Customer Problem

Traditional banking applications provide balances and transaction
history but often require customers to interpret that information
themselves.

Customers may still struggle to answer questions such as:

- How much money is actually available after recurring obligations?
- Where is most of my money going?
- What will a planned purchase do to my available cash?
- What does my current cash-flow position mean in plain language?

FlowWise converts financial data into actionable and understandable
insights.

---

## 3. Product Vision

Move digital banking from:

"Here is your financial data."

to:

"Here is what your financial data means."

FlowWise should help customers understand their financial position
without replacing professional financial advice.

---

## 4. Target Users

### Primary User

Retail banking customers who want a clearer understanding of their
day-to-day financial position.

### Example Needs

- Understand available cash after recurring obligations
- Identify major spending categories
- Evaluate the impact of a planned expense
- Ask natural-language questions about available financial data

---

## 5. MVP Scope

The FlowWise MVP includes:

### Financial Dashboard

Display:

- Monthly income
- Monthly expenses
- Checking balance
- Savings balance
- Net monthly cash flow
- Available-to-spend amount

### Transaction Intelligence

The system reads synthetic transaction data and:

- Groups spending by category
- Identifies major spending categories
- Identifies predefined recurring obligations

### Cash-Flow Intelligence

Python calculates:

- Total income
- Total expenses
- Net cash flow
- Recurring obligations
- Available-to-spend amount

### Planned Purchase Analysis

Customers can enter a planned purchase amount.

Python calculates:

- Remaining available cash
- Adjusted monthly cash flow

### AI Financial Assistant

Customers can ask natural-language questions about their financial
information.

The AI receives verified financial context produced by the
deterministic calculation layer and generates a plain-language
explanation.

---

## 6. AI Product Principles

FlowWise separates deterministic financial computation from
generative AI.

### Deterministic Layer

Responsible for:

- Balances
- Income calculations
- Expense calculations
- Cash-flow calculations
- Recurring obligation calculations
- Planned purchase calculations

### Generative AI Layer

Responsible for:

- Natural-language explanations
- Financial-data summaries
- Conversational interaction
- Explaining calculated results

The AI is not the system of record for financial calculations.

---

## 7. AI Guardrails

FlowWise AI must:

- Use only supplied financial context
- Avoid inventing balances or transactions
- Avoid generating unsupported credit information
- Clearly identify insufficient information
- Avoid presenting itself as a financial advisor
- Avoid recommending specific financial products or investments
- Explain important limitations when relevant

---

## 8. Non-Goals for MVP

The MVP will not:

- Connect to real bank accounts
- Execute financial transactions
- Transfer money
- Provide investment recommendations
- Determine credit scores
- Approve loans
- Replace professional financial advice

All financial data used by the MVP is synthetic.

---

## 9. Success Metrics

Potential production metrics include:

### Adoption

- Percentage of eligible customers using FlowWise
- AI assistant activation rate

### Engagement

- Financial questions per active user
- Planned-purchase analyses per user
- Repeat usage

### Customer Value

- Percentage of users interacting with generated insights
- User-reported usefulness of explanations
- Percentage of insights leading to follow-up engagement

### AI Quality

- Unsupported-answer rate
- Grounded-response rate
- User feedback on AI explanations
- Percentage of questions where insufficient data is correctly identified

### Reliability

- AI service availability
- Calculation-service availability
- AI fallback rate

---

## 10. Key Risks

### AI Hallucination

Risk:
The AI may generate unsupported financial information.

Mitigation:
Ground responses using deterministic financial outputs and explicit
prompt guardrails.

### Customer Over-Reliance

Risk:
Customers may interpret AI explanations as professional financial
advice.

Mitigation:
Use neutral language, disclose limitations, and avoid prescriptive
investment or lending recommendations.

### Sensitive Financial Data

Risk:
Financial information requires strong privacy and security controls.

Mitigation:
Use synthetic data for the prototype. A production architecture would
require encryption, access controls, consent management, data
minimization, and audit logging.

### AI Service Dependency

Risk:
The external AI service may become unavailable.

Mitigation:
Core calculations remain independent of the AI service and continue to
function when AI explanations are unavailable.

---

## 11. MVP Architecture

Customer
    |
Streamlit UI
    |
Python Application
    |
Pandas Financial Processing
    |
Deterministic Calculation Layer
    |
Structured Financial Context
    |
Generative AI
    |
Customer Explanation

---

## 12. Future Roadmap

Potential future capabilities:

- Automated recurring-payment detection
- Cash-flow forecasting
- Spending anomaly detection
- Savings goals
- Personalized alerts
- Multi-account aggregation
- Explainability and source attribution
- User feedback loop for AI responses
- AI observability and evaluation framework