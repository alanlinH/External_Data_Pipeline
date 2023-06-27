import os
from Find_Panel_Product import Find_panel_product
from Download_PDF import Download_PDF

class External_data_pipeline():
    def __init__(self,company):
        self.company = company

    def external_data_pipeline(self):
        save_path = "./PDF/"+self.company+"/"
        if not os.path.isdir(save_path):
            os.mkdir(save_path)

        sku_name = Find_panel_product(company_name).find_panel_product()
        sku_name = sku_name.replace("\n","").split(', ')
        print(company_name,' sku_name :',sku_name)    

        for sku in sku_name:
            download = Download_PDF(save_path,self.company,sku)
            url_list = download.search_SKU()
            download.download_PDF(url_list)

if __name__ == '__main__':
    company_name = "Riken Keiki" #Control4
    External_data_pipeline(company_name).external_data_pipeline()