terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 2.92"
    }
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name = "lv21_wistiwistisen_projectexercise"
}

resource "azurerm_service_plan" "main" {
 name = "terraformed-asp" 
 location = data.azurerm_resource_group.main.location 
 resource_group_name = data.azurerm_resource_group.main.name 
 os_type = "Linux"
 sku_name = "B1"
}
resource "azurerm_linux_web_app" "main" {
 name = "Terra-Chaos-Todo" 
 location = data.azurerm_resource_group.main.location 
 resource_group_name = data.azurerm_resource_group.main.name 
 service_plan_id = azurerm_service_plan.main.id 
 site_config { 
 application_stack { 
 docker_image = "appsvcsample/python-helloworld" 
 docker_image_tag = "latest" 
 } 
 } 
 app_settings = { 
 "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io" 
 }
}