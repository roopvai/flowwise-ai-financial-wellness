import streamlit as st
import pandas as pd
import re
from openai import OpenAI
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)
# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="FlowWise",
    page_icon="💰",
    layout="wide"
)

# -----------------------------------
# LOAD SYNTHETIC BANKING DATA
# -----------------------------------

transactions = pd.read_csv("data/transactions.csv")

# -----------------------------------
# FINANCIAL CALCULATIONS
# -----------------------------------

income = transactions[
    transactions["type"] == "income"
]["amount"].sum()

expenses = transactions[
    transactions["type"] == "expense"
]["amount"].sum()

net_cash_flow = income - expenses

# Synthetic opening account balances
checking_balance = 4850
savings_balance = 12400

# Reserve money for upcoming obligations
# Categories considered recurring financial obligations
recurring_categories = [
    "Housing",
    "Utilities",
    "Subscription"
]

# Certain known recurring payments
recurring_merchants = [
    "Car Payment"
]

recurring_transactions = transactions[
    (transactions["category"].isin(recurring_categories))
    | (transactions["merchant"].isin(recurring_merchants))
]

upcoming_obligations = recurring_transactions["amount"].sum()

available_to_spend = checking_balance - upcoming_obligations

# -----------------------------------
# FLOWWISE DASHBOARD
# -----------------------------------

st.title("💰 FlowWise")
st.subheader("Intelligent Financial Wellness")

st.caption("AI-enabled cash-flow intelligence using synthetic banking data")

st.divider()

# -----------------------------------
# ACCOUNT OVERVIEW
# -----------------------------------

st.header("Financial Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Available to Spend",
        f"${available_to_spend:,.0f}"
    )

with col2:
    st.metric(
        "Monthly Income",
        f"${income:,.0f}"
    )

with col3:
    st.metric(
        "Monthly Expenses",
        f"${expenses:,.0f}"
    )

# -----------------------------------
# CASH FLOW
# -----------------------------------

st.header("Cash Flow")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Checking",
        f"${checking_balance:,.0f}"
    )

with col2:
    st.metric(
        "Savings",
        f"${savings_balance:,.0f}"
    )

with col3:
    st.metric(
        "Net Monthly Cash Flow",
        f"${net_cash_flow:,.0f}"
    )
# -----------------------------------
# RECURRING OBLIGATIONS
# -----------------------------------

st.header("Upcoming Obligations")

obligations_display = recurring_transactions[
    ["merchant", "category", "amount"]
].copy()

obligations_display["amount"] = obligations_display[
    "amount"
].apply(lambda x: f"${x:,.2f}")

st.dataframe(
    obligations_display,
    use_container_width=True,
    hide_index=True
)

st.caption(
    f"Total identified obligations: ${upcoming_obligations:,.0f}"
)
# -----------------------------------
# TRANSACTIONS
# -----------------------------------

st.header("Recent Transactions")

display_transactions = transactions.copy()

display_transactions["amount"] = display_transactions[
    "amount"
].apply(lambda x: f"${x:,.2f}")

st.dataframe(
    display_transactions,
    use_container_width=True,
    hide_index=True
)

# -----------------------------------
# SPENDING BY CATEGORY
# -----------------------------------

st.header("Spending by Category")

expense_data = transactions[
    transactions["type"] == "expense"
]

category_spending = (
    expense_data
    .groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_spending)

# -----------------------------------
# FINANCIAL INSIGHTS
# -----------------------------------

st.header("💡 FlowWise Insights")

largest_category = category_spending.idxmax()

largest_category_amount = category_spending.max()

st.info(
    f"Your largest spending category this month is "
    f"{largest_category} at ${largest_category_amount:,.0f}."
)

st.success(
    f"Your current monthly net cash flow is "
    f"${net_cash_flow:,.0f}."
)

# -----------------------------------
# UPCOMING PRODUCT FEATURE
# -----------------------------------

# -----------------------------------
# CAN I AFFORD IT?
# -----------------------------------

st.header("💳 Can I Afford It?")

st.write(
    "See how a planned purchase could affect your available cash."
)

purchase_name = st.text_input(
    "What are you planning to buy?",
    placeholder="Example: Vacation"
)

purchase_amount = st.number_input(
    "Estimated cost ($)",
    min_value=0.0,
    step=50.0
)

if st.button("Analyze Purchase"):

    remaining_after_purchase = (
        available_to_spend - purchase_amount
    )

    if purchase_amount == 0:
        st.warning("Enter a purchase amount to analyze.")

    elif remaining_after_purchase >= 500:

        st.success(
            f"Based on your current cash flow, "
            f"a ${purchase_amount:,.0f} {purchase_name} "
            f"would leave approximately "
            f"${remaining_after_purchase:,.0f} available "
            f"after identified obligations."
        )

    elif remaining_after_purchase >= 0:

        st.warning(
            f"This purchase would leave only "
            f"${remaining_after_purchase:,.0f} available "
            f"after identified obligations."
        )

    else:

        st.error(
            f"This purchase exceeds your currently "
            f"available amount by "
            f"${abs(remaining_after_purchase):,.0f}."
        )
        # -----------------------------------
# -----------------------------------
# AI FINANCIAL ASSISTANT V2
# -----------------------------------

st.divider()

st.header("🤖 Ask FlowWise")

st.write(
    "Ask questions about your finances. FlowWise uses "
    "deterministic financial calculations combined with "
    "AI-generated explanations."
)

ai_question = st.text_input(
    "What would you like to know?",
    placeholder="Example: Can I afford a $700 vacation?",
    key="ai_question"
)

if st.button("Ask FlowWise"):

    if not ai_question:
        st.warning("Please enter a question.")

    else:

        # -----------------------------------
        # STEP 1: EXTRACT PURCHASE AMOUNT
        # -----------------------------------

        amount_match = re.search(
            r"\$?\s*([\d,]+(?:\.\d{1,2})?)",
            ai_question
        )

        purchase_amount_ai = None
        remaining_after_purchase_ai = None
        adjusted_cash_flow = None

        if amount_match:

            purchase_amount_ai = float(
                amount_match.group(1).replace(",", "")
            )

            # Python performs all financial calculations
            remaining_after_purchase_ai = (
                available_to_spend - purchase_amount_ai
            )

            adjusted_cash_flow = (
                net_cash_flow - purchase_amount_ai
            )

        # -----------------------------------
        # STEP 2: BUILD TRUSTED CONTEXT
        # -----------------------------------

        financial_context = f"""
        VERIFIED FLOWWISE DATA

        Monthly income: ${income:,.2f}
        Monthly expenses: ${expenses:,.2f}
        Net monthly cash flow: ${net_cash_flow:,.2f}

        Checking balance: ${checking_balance:,.2f}
        Savings balance: ${savings_balance:,.2f}

        Identified recurring obligations:
        ${upcoming_obligations:,.2f}

        Available to spend after obligations:
        ${available_to_spend:,.2f}

        Largest spending category:
        {largest_category} at
        ${largest_category_amount:,.2f}
        """

        # Add deterministic purchase calculations
        # only when an amount was detected.

        if purchase_amount_ai is not None:

            financial_context += f"""

            PURCHASE ANALYSIS CALCULATED BY PYTHON

            Planned purchase:
            ${purchase_amount_ai:,.2f}

            Remaining available after purchase:
            ${remaining_after_purchase_ai:,.2f}

            Adjusted monthly cash flow:
            ${adjusted_cash_flow:,.2f}
            """

        # -----------------------------------
        # STEP 3: AI GUARDRAILS
        # -----------------------------------

        prompt = f"""
        You are FlowWise AI, the explanation layer for
        a financial wellness prototype.

        The financial values below were calculated by
        deterministic Python logic.

        {financial_context}

        CUSTOMER QUESTION:
        {ai_question}

        IMPORTANT RULES:

        1. Use only the supplied FlowWise data.

        2. Do not perform new financial calculations.

        3. Do not invent financial information.

        4. Do not invent credit scores, transactions,
           balances, debts, income, or financial history.

        5. When a calculated purchase analysis is supplied,
           explain those calculated results.

        6. Do not say that the customer definitely
           "can afford" a purchase.

           Instead say:
           "Based on the financial data currently available,
           this purchase fits within your available-to-spend
           amount."

        7. Mention important limitations when appropriate.

        8. If the provided data cannot answer the question,
           clearly say that there is not enough information.

        9. Do not recommend specific investments,
           securities, loans, or financial products.

        10. Keep the explanation concise and understandable.
        """

        # -----------------------------------
        # STEP 4: CALL AI
        # -----------------------------------

        try:

            with st.spinner(
                "FlowWise is analyzing your financial data..."
            ):

                response = client.responses.create(
                    model="gpt-5.6-luna",
                    input=prompt
                )

            st.subheader("FlowWise AI")

            st.write(response.output_text)

            # -----------------------------------
            # SHOW VERIFIED CALCULATIONS
            # -----------------------------------

            if purchase_amount_ai is not None:

                st.subheader("Verified Calculation")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Planned Purchase",
                        f"${purchase_amount_ai:,.0f}"
                    )

                with col2:
                    st.metric(
                        "Remaining Available",
                        f"${remaining_after_purchase_ai:,.0f}"
                    )

                with col3:
                    st.metric(
                        "Adjusted Cash Flow",
                        f"${adjusted_cash_flow:,.0f}"
                    )

            st.caption(
                "AI-generated explanation based on synthetic "
                "financial data. Financial calculations are "
                "performed by deterministic Python logic."
            )

        except Exception:

            st.error(
                "The AI explanation service is temporarily "
                "unavailable. Your FlowWise financial "
                "calculations are still available."
            )