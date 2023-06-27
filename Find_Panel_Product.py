import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class Find_panel_product:
    def __init__(self,company): 
        self.company = company

    def find_panel_product(self):
        # business_Group_response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt="請以list格式輸出，"+ self.company +"有哪些事業群",
        #     max_tokens=1280,
        #     temperature=0.1,
        # )
        # print("business_Group_response :",business_Group_response["choices"][0]["text"])
        panel_product_response = openai.Completion.create(
            model="text-davinci-003",
            prompt="請用,分隔列出，"+ self.company +"的產品中，可能具有顯示螢幕的產品系列英文名稱",
            max_tokens=400,
            temperature=0.2,
        )
        # print("panel_product_response :",panel_product_response["choices"][0]["text"])
        completed_text = panel_product_response["choices"][0]["text"]
        return completed_text
    
if __name__ == '__main__':
    company_name = "Riken Keiki"
    sku_name = Find_panel_product(company_name).find_panel_product()
    print(company_name,' sku_name :',sku_name)    