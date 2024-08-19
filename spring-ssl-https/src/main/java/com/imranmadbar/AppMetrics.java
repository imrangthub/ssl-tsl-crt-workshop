package com.imranmadbar;

public class AppMetrics {
	
	
	Boolean appReady = true;
	
	int appHealth = 60;

	public Boolean getAppReady() {
		return appReady;
	}

	public void setAppReady(Boolean appReady) {
		this.appReady = appReady;
	}

	public int getAppHealth() {
		return appHealth;
	}

	public void setAppHealth(int appHealth) {
		this.appHealth = appHealth;
	}

	@Override
	public String toString() {
		return "AppMetrics [appReady=" + appReady + ", appHealth=" + appHealth + "]";
	}



	
	
	

	
}
