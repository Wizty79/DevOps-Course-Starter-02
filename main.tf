terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 2.92"
    }
  }
    backend "azurerm" {
    resource_group_name  = "LV21_WistiWistisen_ProjectExercise"
    storage_account_name = "chaoskept14588"
    container_name       = "chaoscontained"
    key                  = "prod.terraform.tfstate"
  }

}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name = "LV21_WistiWistisen_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "terraformed-chaos"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}
resource "azurerm_linux_web_app" "main" { 
  name                = "TerraBerra-Chaos-Todo"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id
  site_config {
    application_stack {
      docker_image     = "wizty79/wi79_images"
      docker_image_tag = "latest"
    }
  }
  app_settings = {
    "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"  
    "PRIMARY_CONNECTION_STRING_DB"  = azurerm_cosmosdb_account.db.connection_strings[0]
    "REDIRECT_URL" = "https://TerraBerra-Chaos-Todo.azurewebsites.net/callback"
    "DOCKER_TOKEN" = var.DOCKER_TOKEN
    "DOCKER_USERNAME" = "wizty79"
    "GITHUB_TERRA_CLIENT_ID" = var.GITHUB_TERRA_CLIENT_ID
    "GITHUB_TERRA_CLIENT_SECRET" = var.GITHUB_TERRA_CLIENT_SECRET
    "SECRET_KEY" = var.SECRET_KEY

  }
}

resource "azurerm_cosmosdb_account" "db" {
  name = "chaos-cosmos-db"
  location = "UK South"
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
    location          = "westus"
    failover_priority = 0
  }
  # lifecycle {  #ask: Jack said to destroy after each gitpod session??
  #  prevent_destroy = true 
  #}
}

resource "azurerm_cosmosdb_mongo_database" "main" {
  name = azurerm_cosmosdb_account.db.name
  resource_group_name = data.azurerm_resource_group.main.name
  account_name = azurerm_cosmosdb_account.db.name

}

