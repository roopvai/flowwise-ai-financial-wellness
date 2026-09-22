# FlowWise Program Risk Register

## Purpose

This register identifies key product, technical, AI, security, and
delivery risks for the FlowWise financial wellness platform.

| ID | Risk | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|---|
| R1 | AI generates unsupported financial information | High | Medium | Ground responses using verified financial context and explicit AI guardrails | AI/Product |
| R2 | AI contradicts deterministic calculations | High | Medium | Keep Python as source of truth and evaluate responses for numerical consistency | Engineering/AI |
| R3 | Sensitive financial data exposure | Critical | Medium | Encryption, access control, data minimization, secrets management and audit logging | Security |
| R4 | External AI service unavailable | Medium | Medium | Maintain core financial calculations independently and provide graceful degradation | Engineering |
| R5 | AI latency negatively impacts UX | Medium | Medium | Monitor latency, set timeouts and maintain non-AI functionality | Engineering |
| R6 | AI API usage creates unexpected cost | Medium | Medium | Monitor token usage, establish budgets and optimize context sent to the model | TPM/Engineering |
| R7 | Recurring transactions incorrectly identified | Medium | Medium | Start with deterministic rules and introduce user correction/feedback mechanisms | Product/Data |
| R8 | Customer interprets AI explanation as financial advice | High | Medium | Use neutral language, disclose limitations and restrict prescriptive recommendations | Product/Legal |
| R9 | Regulatory/compliance requirements delay production launch | High | Medium | Engage Legal, Risk, Privacy and Compliance early in product development | TPM/Compliance |
| R10 | Scope expands beyond MVP | Medium | High | Maintain explicit MVP/non-goal definitions and evaluate new features against launch objectives | TPM |
| R11 | Poor AI responses reduce customer trust | High | Medium | Establish evaluation dataset, feedback mechanisms and response-quality monitoring | AI/Product |
| R12 | Banking-data integration dependency delays production implementation | High | Medium | Define API contracts early and use synthetic data to decouple prototype development | TPM/Engineering |

## Highest-Priority Risks

### 1. AI Groundedness

Financial applications require a high level of customer trust.

FlowWise reduces hallucination exposure by separating deterministic
financial calculations from generative explanations.

### 2. Data Privacy and Security

The current MVP uses only synthetic financial data.

A production implementation would require additional controls including
encryption, authentication, authorization, consent management,
auditability and data-retention policies.

### 3. External AI Dependency

FlowWise should not become unavailable because an external AI service
fails.

The financial dashboard and deterministic calculation engine therefore
operate independently from the generative AI service.

### 4. Regulatory and Compliance Dependencies

A production banking implementation would require review by appropriate
legal, privacy, risk and compliance stakeholders before launch.

## Risk Review Process

For a production program, risks would be reviewed regularly during
program execution.

The TPM would coordinate:

- Risk identification
- Impact and likelihood assessment
- Mitigation ownership
- Dependency escalation
- Decision tracking
- Executive visibility for high-impact risks

Risks would be updated as architecture, scope and external dependencies
change.