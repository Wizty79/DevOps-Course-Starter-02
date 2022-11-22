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

##https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/cosmosdb_account
##to be adapted

resource "azurerm_resource_group" "main" {
  name     = data.azurerm_resource_group.main.name
  location = "UK South" 
}

resource "random_integer" "ri" {
  min = 10000
  max = 99999
}

resource "azurerm_cosmosdb_account" "db" {
  name                = "tfex-cosmos-db-${random_integer.ri.result}"
  #location            = azurerm_resource_group.example.location
  location            = "UK South"
  #resource_group_name = azurerm_resource_group.example.name
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"

  enable_automatic_failover = true
  
  capabilities { 
	name = "EnableServerless" 
  }

  capabilities {
    name = "EnableAggregationPipeline"
  }

  capabilities {
    name = "mongoEnableDocLevelTTL"
  }

  capabilities {
    name = "MongoDBv3.4"
  }

  capabilities {
    name = "EnableMongo"
  }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }

  geo_location {
    location          = "eastus"
    failover_priority = 1
  }

  geo_location {
    location          = "westus"
    failover_priority = 0
  }
}

##https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/cosmosdb_mongo_database

data "azurerm_cosmosdb_account" "main" {
  #name                = "tfex-cosmosdb-account"
  name                = "chaostododb"
  #resource_group_name = "tfex-cosmosdb-account-rg"
  resource_group_name = data.azurerm_resource_group.main.name
}

resource "azurerm_cosmosdb_mongo_database" "main" {
  name                = "tfex-cosmos-mongo-db"
  #resource_group_name = data.azurerm_cosmosdb_account.example.resource_group_name
  resource_group_name = data.azurerm_resource_group.main.name
  #account_name        = data.azurerm_cosmosdb_account.example.name
  account_name        = data.azurerm_cosmosdb_account.main.name
  throughput          = 400
}