variable "API_KEY" {
	type = string
	sensitive = true
}

variable "API_TOKEN" {
	type = string
	sensitive = true
}

variable "REDIRECT_URI" {
	type = string
	default = "https://TerraBerra-Chaos-Todo.azurewebsites.net/callback"
}

variable "USERNAME" {
	type = string
	sensitive = true
	default = "chaostododb" # should this be chaos-cosmos-db?
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

variable "GITHUB_CLIENT_ID" {
	type = string
	sensitive = true
}

variable "GITHUB_CLIENT_SECRET" {
	type = string
	sensitive = true
}

variable "SECRET_KEY" {
	type = string
	sensitive = true
}

