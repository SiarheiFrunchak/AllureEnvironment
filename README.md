# AllureEnvironment

Script for generation the **environment.properties** file, according with pipeline configuration and dependencies


### How to use:
 - `$TEST_STEND_HOST` and `$TEST_STEND_PORT` should be passed into environment variables or `reference.conf` file
 - Before start usage don't forget to update script with correct cobfiguration `get_runner_type()`
 - After file generation, **environment.properties** file should be moved into `allure-results` direcotory
 - Generate allure report `allure generate ./allure-results -o ./allure-report --clean`
 
