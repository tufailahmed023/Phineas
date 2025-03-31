# Phineas
 Develop a company-wide chatbot capable of aligning and answering IT and HR policy-related queries.

## How to run locally 
-   Create a new env by 
```bash 
conda create -n env_name python=3.10
```
-   Install all requrements by 
```bash 
pip install -r requirements.txt
```
-   Create a ```.env``` file 
Instert your OpenAi API key in like ```OPENAI_API_KEY = ""```

- Run Streamlit 
```bash 
streamlit run app.py
```

## Errors 
If you encounter an error "local variable 'text' referenced before assignment" then just delete the file present in extracted_texts. 
