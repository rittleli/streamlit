import streamlit as st

def predidct_value(p_storm, sensitivity, specificity, payout_of_harvest, payout_of_no_harvest_storm, payout_of_no_harvest_and_no_storm):
    p_dns = (specificity * (1 - p_storm) + p_storm * (1 - specificity))
    p_ns_dns = specificity * (1 - p_storm) / p_dns
    p_ds = (sensitivity * p_storm) + ( 1 - p_storm) * (1 - sensitivity)
    p_s_ds = (sensitivity * p_storm) / p_ds
    value_no_storm = max(payout_of_harvest, p_ns_dns * payout_of_no_harvest_and_no_storm + (1 - p_ns_dns) * payout_of_no_harvest_storm)
    value_storm = max(payout_of_harvest, p_s_ds * payout_of_no_harvest_storm + payout_of_no_harvest_and_no_storm * (1 - p_s_ds))
    value_no_harvest = p_dns * value_no_storm + p_ds* value_storm
    return value_no_harvest, abs(value_no_harvest - payout_of_harvest)

chance_of_botryis = st.number_input('Chance of botrytis(Please input a value from 0.0 to 1.0, default value 0.1)', min_value=0.0, max_value=1.0, value=0.1)
payout_of_no_harvest_storm = chance_of_botryis * 3300000 + (1 - chance_of_botryis) * 420000
chance_of_high = st.number_input('Chance of high sugar level(Please input a value from 0.0 to 1.0)', min_value=0.0, max_value=1.0 , value=0.1)
chance_of_typical = st.number_input('Chance of typical sugar level(Please input a value from 0.0 to 1.0)', min_value=0.0, max_value=1 - chance_of_high , value=0.3)
chance_of_no = st.number_input('Chance of no sugar level(Please input a value from 0.0 to 1.0)', min_value=0.0, max_value=1 - chance_of_high -chance_of_typical, value=1-chance_of_high - chance_of_typical)
payout_of_no_harvest_and_no_storm = chance_of_high * 1500000 + chance_of_typical * 1410000 + chance_of_no * 960000

# Use the predict_price function to get a prediction based on the user input
prediction, value_of_clairvoyance = predidct_value(0.5, 0.09, 0.92, 960000, payout_of_no_harvest_storm, payout_of_no_harvest_and_no_storm)


# Display the prediction to the user
st.write(f'The e-value of the using a prediction model is ${prediction:,.2f}')
if value_of_clairvoyance > 0:
    st.write(f'Plase use a prediction model')
else:
    st.write(f'Plase harvest now.')