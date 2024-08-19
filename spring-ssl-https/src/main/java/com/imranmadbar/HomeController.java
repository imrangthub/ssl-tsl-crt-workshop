package com.imranmadbar;

import java.io.IOException;

import javax.servlet.http.HttpServletResponse;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HomeController {

	Logger logger = LoggerFactory.getLogger(HomeController.class);

	@GetMapping(value = "/")
	public String welcomeMsg() {
		logger.info("Welcome to SpringBootSslTlsCertApplication");
		return "Welcome to SpringBootSslTlsCertApplication";
	}

	@GetMapping(value = "/home")
	public String welcomeMsgHome() {
		logger.info("Welcome to SpringBootSslTlsCertApplication Home");
		return "Welcome to SpringBootSslTlsCertApplication Home";
	}

	@GetMapping(value = "/metrics", produces = "text/plain")
	public void metrics(HttpServletResponse response) throws IOException {
		// Replace these with actual values from your application's logic
		boolean appReady = true; // Or whatever logic determines readiness
		int appHealth = 80; // Your app's health metric

		// Format the metrics in Prometheus text format
		String metricsData = String
				.format("# HELP app_ready Indicates if the application is ready (1 for true, 0 for false)\n"
						+ "# TYPE app_ready gauge\n" + "app_ready %d\n\n"
						+ "# HELP app_health Current health status of the application\n" + "# TYPE app_health gauge\n"
						+ "app_health %d\n", appReady ? 1 : 0, appHealth);

		// Write the response
		response.getWriter().write(metricsData);
	}

}
