
package com.xgqfrms.tag;
 
import com.xgqfrms.tag.config.ApplicationProperties;
import java.net.InetAddress;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.core.env.Environment;
 
@Slf4j
@SpringBootApplication
@EnableConfigurationProperties(ApplicationProperties.class)
public class Application {
 
  private final Environment env;
 
  public Application(Environment env) {
    this.env = env;
  }
 
  public static void main(String[] args) {
 
    SpringApplication app = new SpringApplication(Application.class);
    Environment env = app.run(args).getEnvironment();
    String protocol = "http";
    if (env.getProperty("server.ssl.key-store") != null) {
      protocol = "https";
    }
    String hostAddress = "localhost";
    try {
      hostAddress = InetAddress.getLocalHost().getHostAddress();
    } catch (Exception e) {
      log.warn("The host name could not be determined, using `localhost` as fallback");
    }
    log.info("\n----------------------------------------------------------\n\t" +
            "Application '{}' is running! Access URLs:\n\t" +
            "Local: \t\t{}://localhost:{}\n\t" +
            "External: \t{}://{}:{}\n\t" +
            "Profile(s): \t{}\n----------------------------------------------------------",
        env.getProperty("spring.application.name"),
        protocol,
        env.getProperty("server.port"),
        protocol,
        hostAddress,
        env.getProperty("server.port"),
        env.getActiveProfiles());
  }
 
}

