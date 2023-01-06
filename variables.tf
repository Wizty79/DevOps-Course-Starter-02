variable "API_KEY" {
	type = string
	sensitive = true
}

variable "API_TOKEN" {
	type = string
	sensitive = true
}

variable "REDIRECT_URL" {
	type = string
	default = "https://TerraBerra-Chaos-Todo.azurewebsites.net/callback"
	#default = https://localhost:5000/callback
}

variable "USERNAME" {
	type = string
	sensitive = true
	default = "chaos-cosmos-db" # database name? 
}

variable "DOCKER_TOKEN" {
	type = string
	sensitive = true
}

variable "DOCKER_USERNAME" {
	type = string
	sensitive = true
	default = "wizty79"
}

variable "GITHUB_TERRA_CLIENT_ID" {
	type = string
	sensitive = true
}

variable "GITHUB_TERRA_CLIENT_SECRET" {
	type = string
	sensitive = true
}

variable "SECRET_KEY" {
	type = string
	sensitive = true
}

