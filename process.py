import streamlit as st
import pandas as pd
from io import BytesIO

st.title("📊 Salary Voucher Processor (JK-Central Pulp Mill)")


# Profit Mapping

profit_maping = {
    21132202 : 210010, 21142101 : 210010, 21151101 : 210010, 21151201 : 210010,
    21151202 : 210010, 21152101 : 210010, 21153102 : 210010, 21154101 : 210010,
    21154102 : 210010, 21154104 : 210010, 21161101 : 210020, 21161202 : 210020,
    21161204 : 210020, 21162101 : 210020, 21162201 : 210020, 21163101 : 210020,
    21171101 : 210010, 21172101 : 210020, 21311001 : 210010, 21311002 : 210010,
    21311003 : 210010, 21311004 : 210010, 21311005 : 210010, 21311007 : 210010,
    21321001 : 210010, 21321002 : 210010, 21321003 : 210010, 21321006 : 210010,
    21321009 : 210010, 21331004 : 210010, 21331005 : 210010, 21331007 : 210010,
    21331008 : 210010, 21331010 : 210010, 21332001 : 210020, 21341001 : 210010,
    21342002 : 210020, 22111101 : 220020, 22132101 : 220020, 22132202 : 220020,
    22144101 : 220020, 22144202 : 220020, 22162101 : 220020, 22163101 : 220020,
    22164101 : 220020, 22164201 : 220020, 22164202 : 220020, 22164204 : 220020,
    22172101 : 220020, 22221101 : 220020, 22221202 : 220020, 22241101 : 220020,
    22311002 : 220030, 22331005 : 220020, 22342001 : 220020, 31041001 : 310010,
    31051001 : 310010, 31061001 : 310010, 31043001 : 310020, 22331009 : 220020

}

# Calculation Groups

calc_groups = {
    #earnings
    "Earnings_Basic": ["1000", "1001", "1003"],
    "Earnings_Allowance": ["1050", "1051", "1053"],
    "Earnings_Special Allowance": ["1060", "1061", "1063"],
    "Earnings_Conveyance": ["1070", "1071", "1073"],
    "Earnings_Education Allowance": ["1080", "1081", "1083"],
    "Earnings_Medical Allowance": ["1090", "1091", "1093"],
    "Earnings_HRA": ["1120", "1121", "1123"],
    "Earnings_Amt InLieu": ["1130", "1131", "1133"],
    "Earnings_Production Inc": ["1220", "1221", "1223"],
    "Earnings_Electricity Reba": ["1460", "1461"],
    "Earnings_Variable Pay": ["1550", "1551"],
    "Earnings_Other Allowance": ["1660", "1661", "1663"],
    "Earnings_Leave Encashment":["1690","1691"],
    "Earnings_Other": ["1730","1731"],
    #deductions
    "Deductions_Compulsory PF Payable": ["/3F1", "/3F2","9F13", "9F23"],
    "Deductions_Prof Tax Payable": ["/3P3"],
    "Deductions_Labour Welfare Fund Payable": ["3W1","13W1"],
    "Deductions_Tds-Salaries Sec 192": ["/460"],
    "Deductions_MCS Allowances": ["/563"],
    "Deductions_Employee Adv  Salary": ["00RP"],
    "Deductions_Employee Adv  Med,Edu,etc": ["01RP"],
    "Deductions_Employee Adv  Vehicle": ["03RP"],
    "Deductions_Bank Loan Recovery": ["04RP"],
    "Deductions_Emp_Co-Op_Sc_LoanInterest": ["06ID"],
    "Deductions_Emp_Co-Op_Sc_Regular_Rep_So_06RP": ["06RP"],
    "Deductions_Emp_Co-Op_Sc_Arr_Loan_Inter":["26ID"],
    "Deductions_Employee Adv Vehicle_Regular_Rep_Tw": ["07RP"],
    "Deductions_Employee Adv Vehicle_Regular_Rep_Ca": ["08RP"],
    "Deductions_Emp_Co-Op_Sc_Regular_Rep_So_10RP": ["10RP"],
    "Deductions_LPS Public School":["7030"],
    "Deductions_Taxi Hire Charges-7050": ["7050"],
    "Deductions_Electricity Charges Realised": ["7060","7061"],
    "Deductions_Guest House Expenses":["7070"],
    "Deductions_Officers Club_Gym": ["7270"],
    "Deductions_Ladies Club": ["7350"],
    "Deductions_Emp Ben Fund": ["7390"],
    "Deductions_Officers Club": ["7400"],
    "Deductions_Sports Club": ["7430"],
    "Deductions_Co-Opeartive Me": ["7450"],
    "Deductions_Furniture Hire": ["7460"],
    "Deductions_MCS WELFARE Coupon": ["7470"],
    "Deductions_Mess Expenses": ["7490"],
    "Deductions_Taxi Hire Charges-7480": ["7480"],
    "Deductions_Prepaid Insurance- Mediclaim": ["7520"],
    "Deductions_Rent recovery from Employee": ["7540","7543"],
    "Deductions_Staff Insurance Payable- LIC": ["7610"],
    "Deductions_Officers Club- Event_OD1": ["7650"],
    "Deductions_Insurance Vehicles- OD2": ["7670"],
    "Deductions_MCS WELFARE- Penalty_OD3": ["7660"],
    "Deductions_MCS WELFARE- Other_OD4": ["7680"],
    "Deductions_MCS WELFARE- NewIDCardIssue": ["7110"],
    "Deductions_Employee Death Benefits": ["7600","7601"]
}
# GL Mapping
gl_mapping = {
    "Earnings_Basic": 4401010700,
    "Earnings_Allowance": 4401010800,
    "Earnings_Special Allowance": 4401010830,
    "Earnings_Conveyance": 4401011800,
    "Earnings_Education Allowance": 4401011900,
    "Earnings_Medical Allowance": 4401012100,
    "Earnings_HRA": 4401011700,
    "Earnings_Amt InLieu": 4401010800,
    "Earnings_Electricity Reba": 4701020500,
    "Earnings_Variable Pay": 2503091200,
    "Earnings_Leave Encashment": 2403010100,
    "Earnings_Production Inc": 4401011200,
    "Earnings_Other Allowance": 4401010800,
    "Earnings_Other": 4401010800,

    "Deductions_Compulsory PF Payable": 2504021200,
    "Deductions_Prof Tax Payable": 2504021500,
    "Deductions_Labour Welfare Fund Payable": 2504021800,
    "Deductions_Tds-Salaries Sec 192": 2504020200,
    "Deductions_MCS Allowances": 4401010800,
    "Deductions_Employee Adv  Salary": 1207040403,
    "Deductions_Employee Adv  Med,Edu,etc": 1207040601,
    "Deductions_Employee Adv  Vehicle": 1207040801,
    "Deductions_Bank Loan Recovery": 2503095600,
    "Deductions_Emp_Co-Op_Sc_LoanInterest": 2503092400,
    "Deductions_Emp_Co-Op_Sc_Regular_Rep_So_06RP": 2503092400,
    "Deductions_Emp_Co-Op_Sc_Arr_Loan_Inter": 2503092400,
    "Deductions_Employee Adv Vehicle_Regular_Rep_Tw": 1207040801,
    "Deductions_Employee Adv Vehicle_Regular_Rep_Ca": 1207040801,
    "Deductions_Emp_Co-Op_Sc_Regular_Rep_So_10RP": 2503092400,
    "Deductions_LPS Public School": 2503094900,
    "Deductions_Taxi Hire Charges-7050": 4701195600,
    "Deductions_Electricity Charges Realised": 4701020500,
    "Deductions_Guest House Expenses": 4701193800,
    "Deductions_Officers Club_Gym": 2503092600,
    "Deductions_Ladies Club": 2503094000,
    "Deductions_Emp Ben Fund": 2503093900,
    "Deductions_Officers Club": 2503092600,
    "Deductions_Sports Club": 2503092700,
    "Deductions_Co-Opeartive Me": 2503092400,
    "Deductions_Furniture Hire": 4701193000,
    "Deductions_MCS WELFARE Coupon": 4401030300,
    "Deductions_Taxi Hire Charges-7480": 4701195600,
    "Deductions_Mess Expenses": 4701193800,
    "Deductions_Prepaid Insurance- Mediclaim": 1209010600,
    "Deductions_Rent recovery from Employee": 4401030800,
    "Deductions_Staff Insurance Payable- LIC": 2503090700,
    "Deductions_Officers Club- Event_OD1": 2503092600,
    "Deductions_Insurance Vehicles- OD2": 4701060400,
    "Deductions_MCS WELFARE- Penalty_OD3": 4401030300,
    "Deductions_MCS WELFARE- Other_OD4": 4401030300,
    "Deductions_MCS WELFARE- NewIDCardIssue": 4401030300,
    "Deductions_Employee Death Benefits": 2503093900
}

# Upload salary voucher only

salary_file = st.file_uploader("Upload Salary Voucher Excel", type=["xlsx"])

if salary_file:
    
    # Detect header row automatically
    
    temp_df = pd.read_excel(salary_file,sheet_name=0, header=None)
    header_row = temp_df[temp_df.apply(lambda row: row.astype(str).str.contains("Cost Centre").any(), axis=1)].index[0]
    
    df = pd.read_excel(salary_file, sheet_name=0, header=header_row)
    df.columns = df.columns.map(lambda x: str(x).strip())
    df = df.dropna(subset=["Cost Centre"])
    df["Cost Centre"] = pd.to_numeric(df["Cost Centre"], errors="coerce").fillna(0).astype(int)
    
    
    # main process of voucher
    
    summary_list = []
    for component, codes in calc_groups.items():
        matched_cols = [col for col in df.columns if any(code in str(col) for code in codes)]
        if matched_cols:
            df[matched_cols] = df[matched_cols].apply(pd.to_numeric, errors="coerce").fillna(0)
            df[component] = df[matched_cols].sum(axis=1)
            
            temp = df.groupby("Cost Centre", as_index=False)[component].sum()

            if component.startswith("Deductions"):
                temp[component]= - temp[component]

            temp = temp.rename(columns={component: "Amount"})
            temp["Component"] = component
            temp["Profit Centre"] = temp["Cost Centre"].map(profit_maping).fillna(0).astype(int)
            temp["GL"] = temp["Component"].map(gl_mapping).fillna(0).astype(int)
            
            summary_list.append(temp)
    
    if summary_list:
        summary = pd.concat(summary_list, ignore_index=True)
        summary = summary[["GL", "Cost Centre", "Profit Centre", "Component", "Amount"]]

        net_amount= -summary['Amount'].sum()
        net_row=pd.DataFrame([{
            "GL": 2503090300,
            "Cost Centre": 0,
            "Profit Centre": 210010,
            "Component": "Salary & Wages Payable",
            "Amount": net_amount
        }])
        summary = pd.concat([summary, net_row], ignore_index=True)

    else:
        summary = pd.DataFrame(columns=["GL", "Cost Centre", "Profit Centre", "Component", "Amount"])
    
    st.subheader("Processed Salary Summary")
    st.dataframe(summary)
    
    
    # Download option
    
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        summary.to_excel(writer, sheet_name="Summary", index=False, float_format="%.2f")
    output.seek(0)
    
    st.download_button(
        label="📥 Download Processed Excel",
        data=output,
        file_name="processed_salary_summary.xlsx"
    )



