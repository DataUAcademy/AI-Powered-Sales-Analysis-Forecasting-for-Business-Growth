# AI-Powered-Sales-Analysis-Forecasting-for-Business-Growth

## Overview

The project's main objectives include maximizing revenue, building a forecasting model(LSTM) for future sales and revenue, and optimizing resources for stock preparation and marketing campaigns. The capstone project revolves around leveraging AI for sales analysis and forecasting to support business growth for Olist, a Brazilian e-commerce startup, using Power BI for data visualization. It employs machine learning models like SARIMAX, XGBoost, and LSTM for revenue prediction, with LSTM being the top performer, The integration of a user-friendly Streamlit interface makes the forecasting accessible to stakeholders.

## Data Source
Using Olist E-Commerce dataset as the source of our data (9 csv files). The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. You can find the dataset here [Olist E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## Technologies Used

- Python
- TensorFlow
- Power BI
- Pandas
- NumPy
- Streamlit

## Key Features

- Robust time series forecasting model tailored to capture sales revenue seasonality and trends.
- Interactive Streamlit dashboard for user-friendly data exploration and forecast visualization.
- Clear visual presentation of actual vs. predicted future revenue.
- Interactive data visualization using Power BI for in-depth analysis and insights.
# Data Visualization
## Sales Insight Dashboard

This dashboard provides a clear snapshot of Olist's thriving e-commerce platform, from revenue and logistics to top-selling categories. These insights allow us to optimize our strategies and continue delivering exceptional value to our customers and partners. For full experience and interaction with the dashboard, Here is the link to the dashboard: [AI-Powered Sales Analysis](https://www.novypro.com/project/ai-powered-sales-analysis)

- **Total Revenue**
  "Our total revenue stands at a remarkable $16 million. This is a testament to the robust sales activity on our platform."

- **Total Freight**
  "Logistics is a cornerstone of our operations, with total freight costs amounting to $2.22 million, ensuring timely and reliable delivery of products."

- **Total Orders**
  "The platform has successfully processed 111.02 thousand orders, reflecting the high demand and trust customers place in our services."

- **Total Distinct Orders**
  "Delving deeper, we see that the total number of distinct orders is 97.26 thousand, which indicates a healthy repeat purchase rate among our customer base."
- **Daily Revenue**
  "The line chart for daily revenue shows fluctuations with significant spikes, highlighting key sales events or promotions. For example, a notable peak at $178K is visible, showcasing an exceptional sales day, likely corresponding to the Black Friday sales event."
  
![Sales Dashboard](https://github.com/Famz21/AI-Powered-Sales-Analysis-Forecasting-for-Business-Growth/assets/125658739/ddde9cab-ddae-4fdb-bf2a-f88346813503)

For full experience and interaction with the dashboard, Here is the link to the dashboard: [AI-Powered Sales Analysis](https://www.novypro.com/project/ai-powered-sales-analysis)
## Logistics Dashboard

This logistics overview highlights our platform's extensive reach, efficient order processing, customer-centric payment options, and exceptional delivery performance. These insights enable us to continuously refine our logistics strategies and maintain a high level of service quality.
- **Total Orders by Region**
  "Our platform's reach is extensive, with orders penetrating 4,119 distinct cities across 27 states, demonstrating our widespread presence in the Brazilian market. The map visualization indicates a dense concentration of orders in the southeastern regions, with São Paulo being a vibrant hub for e-commerce activity."
- **Payment Type Popularity**
  "Our customers have a clear preference when it comes to payment methods. An overwhelming 78.34% choose to use credit cards, followed by 17.92% using 'boleto', a popular Brazilian payment method. Vouchers, debit cards, and a few undefined methods make up the remainder. This breakdown is pivotal for tailoring our payment options to customer preferences and ensuring a seamless checkout experience."
- **Total Orders by On-time Delivery**
  "Punctuality is a key performance indicator for our logistics team. We are proud to report that 92.11% of orders were delivered on time, with only 7.89% arriving late. This high rate of on-time delivery underlines our commitment to reliability and customer satisfaction."


![Logistics Dashboard](https://github.com/Famz21/AI-Powered-Sales-Analysis-Forecasting-for-Business-Growth/assets/125658739/da5f077a-37a2-46a8-ba3e-2b53e24c9f13)

For full experience and interaction with the dashboard, Here is the link to the dashboard: [AI-Powered Sales Analysis](https://www.novypro.com/project/ai-powered-sales-analysis)

## Customer Satisfaction

The data from our dashboard reveals a clear correlation between high customer ratings and increased total revenue and order count. The success of products that have achieved a 5-star rating is a testament to our platform's ability to deliver quality products and services, leading to customer delight and repeat business.
- **Total Revenue and Average Review Score**
  "To set the stage, our platform has achieved an impressive $16 million in total revenue, with a noteworthy average review score of 4.09 out of 5. This underscores our commitment to customer satisfaction and high-quality service."

- **Customer Rating VS Order Count & Total Revenue**
  "Delving into the specifics, the composite bar and line chart illustrates a compelling story about customer ratings and their impact on sales. We see a striking increase in both revenue and order count as the review scores ascend. For products rated with 5 stars, the total revenue peaks at $8.8 million with approximately 62 thousand orders. This data point not only signifies high customer satisfaction but also shows that top-rated products are a major revenue driver for our marketplace."



![Customer Satisfaction ](https://github.com/Famz21/AI-Powered-Sales-Analysis-Forecasting-for-Business-Growth/assets/125658739/7b727fcd-dbe3-4b6e-9648-5636c4b93001)

For full experience and interaction with the dashboard, Here is the link to the dashboard: [AI-Powered Sales Analysis](https://www.novypro.com/project/ai-powered-sales-analysis)

# Forecasting
Since the LSTM model demonstrated superior performance, we will utilize it to forecast revenue for the next 3 months. For full experience and interaction with the forecasting web app, Here is the link to the web: [Sales Forecasting with LSTM](https://ai-powered-sales-analysis-forecasting-for-business-growth.streamlit.app/)


![LSTM Forecasting](https://github.com/DataUAcademy/AI-Powered-Sales-Analysis-Forecasting-for-Business-Growth/assets/125658739/28a53aa8-024b-4308-8acf-0aaf5e487529)




After forecasting the revenue for the next 3 months, we observed a downward trend in the line, indicating a negative sign. In response to this forecast, our next step will involve formulating strategic plans and recommendations to address this trend and optimize revenue growth.


# Recommendation & Strategy

Recommendations for Olist

1. **Implement Seasonal/Quarterly Promotional Events:** Olist should implement seasonal or quarterly promotional events, such as "Black Friday" sales, to drive customer engagement, encourage high product purchases, and increase revenue.

2. **Maintain High Product Quality and Competitive Pricing:** It's essential for Olist to maintain high product quality and competitive pricing to minimize cancellations, maximize customer satisfaction, and boost revenue.

3. **Implement Loyalty Programs:** Olist can implement loyalty programs, such as special discounts for repeat customers and free shipping to targeted locations like Sao Paulo and Acre, to drive an increase in repeat purchases, enhance customer retention, and acquire new customers.

4. **Invest in New Products and Services:** With high revenue and profit margins, Olist should consider investing in new products and services and expanding into new markets. This strategy will drive new customer acquisition and ensure Olist stays ahead in the e-commerce business in Brazil.

# Challenges & Limitations

- **Missing Registration Dates:** The dataset does not include information about the registration date of new customers, limiting the depth of customer analysis.

- **Need for Comprehensive Dataset:** To conduct a more sensitive analysis, a longer period dataset is required. This dataset should include additional information such as customer and seller registration dates, as well as customer and seller names.

- **Comparative Analysis:** Obtaining datasets from other similar companies within the same industry would be beneficial for comparison purposes. This comparative analysis can provide insights into industry trends, customer behavior, and business performance.

Addressing these limitations and incorporating additional datasets will contribute to a more robust and insightful analysis, enabling better-informed decision-making processes.

# Future Approach

- **Incorporation of External Factors:** Consider adding external factors such as inflation rate, customer satisfaction, economic indicators, etc., to enhance the model's accuracy and predictive capabilities.

- **Product Category Sales Forecasting:** Extend the model to forecast sales for each product category individually. This granular approach can provide insights into category-specific trends and behaviors.

- **Exploration of Advanced Forecasting Techniques:** Explore advanced forecasting techniques such as FBProphet or ensemble models to leverage the strengths of each approach and potentially achieve higher accuracy in predictions.



 
## Contact & Connect

For further inquiries or to discuss potential collaborations, please feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/rithyvira/).







