package com.imranmadbar;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.core.env.Environment;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
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


}
