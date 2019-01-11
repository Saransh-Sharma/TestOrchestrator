

Read this here:

    https://saransh-sharma.github.io/TestOrchestrator/
    
## Intro to auto testing of Consumer Android App
Automated Functional Tests for Consumer Android app are of 2 kinds:
 - **End to end tests** that cover big flows for things that a typical user would do. 
 These tests span across multiple activities and take 30 - 120 seconds each.
 - **Small functional tests** deal with a small component of an activity or a view. Each of these take 500MS-10 seconds 


The test harness has 2 major components:

- **Test Code** - These are the actual tests, described above. 
Test code lies in a package called androidTest in the 
- **Test Orchestrator** - This helps run the tests. 

## Test orchestrator does the following:
 
 1. **Prep environment for testing**
    - Launch AVDs based upon AVD config file
    - Build app under test and the test apk with the instrumentation tests
 2. **Run tests** 
    - Run sets of tests as specified in the test config file	
    - Shard tests to run across connected devices/AVDs 
    - Identify flaky tests by rerunning any failed tests multiple times. If a failing test passes on some reruns the test can be deemed flaky. If the failing test fails on every rerun, the app under test might be broken. 
 3. **Post test run**
    - Pull and consolidate app logs from device for test report
    - Generate detailed Test Report with:
        * Test run summary with test pass percentage, passed/failed test counts
        * Test session summary session duration, device creation time, apk install time, test rerun time, apk build time
        * Detailed test report with device logs for each test available color coded by severity  
        
    
## How to setup tests to run for the first time?
The steps 1-4 are one time setup. You would have to do these before you run your first tests. 
If you have already set this up please move onto the section that deals with the various commands one can use with the Test Orchestrator.

#### On Cloud device lab
watch this space
#### On local machine

###### 1. **Clone the following 2 repositories:**

Test Orchestrator: This is the test runner

     git@github.com:Saransh-Sharma/TestOrchestrator.git

Consumer Android app: Test code lies here with the app

     git@github.com:Shuttl-Tech/ConsumerAndroid.git
     

###### 2. **Get to the correct branches**

For Test Orchestrator: get to ca_config branch to test ConsumerAndroid app
    
    git checkout ca_config
    
For Consumer app get onto the branch you want to test
    
    git checkout <branch_to_be_tested>
    
###### 3. **Setup paths** 

With is you are all set to run tests on your local machine using the Test Orchestrator.

## Run tests

Cheat sheet to run tests:

|   Command               |Tests run                          |Misc                         |
|--------------------------------------------|-------------------------------|-------------------------------|
|./Launcher.py -tset **AllSanity** -lplan **reBuild**|Runs all End-To-End and Functional tests|Rebuilds app, tests|
|./Launcher.py -tset **AllSanity** -lplan **reRun**  |Runs all End-To-End and Functional tests|Doesn't Rebuild app, tests; runs what it has|
|./Launcher.py -tset **EndToEnd** -lplan **reBuild** |Runs all End-To-End tests only|Rebuilds app, tests|
|./Launcher.py -tset **EndToEnd** -lplan **reRun**   |Runs all End-To-End tests only|Doesn't Rebuild app, tests; runs what it has|
|./Launcher.py -tset **Function** -lplan **reBuild** |Runs all Functional tests only|Rebuilds app, tests|
|./Launcher.py -tset **Function** -lplan **reRun**   |Runs all Functional tests only|Doesn't Rebuild app, tests; runs what it has|


   


## Results
    Sample results:
     
![Test Results Sample](https://raw.githubusercontent.com/Saransh-Sharma/TestOrchestrator/master/ResultsScreenshot.png)
