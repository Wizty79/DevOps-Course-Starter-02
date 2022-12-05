variable "prefix" {
 description = "The prefix used for all resources in this environment"
 default = TF_
}

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
	default = "https://localhost:5000/callback"
}

variable "USERNAME" {
	type = string
	sensitive = true
	default = "chaostododb"
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
