class Settings:
	pass


settings = Settings()

def init_settings(dic: dict):
	for key, value in dic.items():
		setattr(settings, key, value)
	pass