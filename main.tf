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

