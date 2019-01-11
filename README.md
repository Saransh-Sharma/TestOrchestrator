



## Intro
Automated Functional Testing for Consumer Android app

Test orchestrator does the following:
 
 1. Prep environment for testing
    - Launch AVDs based upon AVD config file
    - Build app under test and the test apk with the instrumentation tests
 2. Run tests 
    - Run sets of tests as specified in the test config file	
    - Shard tests to run across connected devices/AVDs 
    - Identify flaky tests by rerunning any failed tests multiple times. If a failing test passes on some reruns the test can be deemed flaky. If the failing test fails on every rerun, the app under test might be broken. 
 3. Post test run
    - Pull and consolidate app logs from device for test report
    - Generate detailed Test Report with:
        * Test run summary with test pass percentage, passed/failed test counts
        * Test session summary session duration, device creation time, apk install time, test rerun time, apk build time
        * Detailed test report with device logs for each test available color coded by severity  
        
    

## Results
    Sample results:
     
![Test Results Sample](https://raw.githubusercontent.com/Saransh-Sharma/TestOrchestrator/master/ResultsScreenshot.png)
