Testing Philosphy
    How thorough
        Wanted to test a bunch, low on time. 
        2-4 tests per function
        Goal: have at least 1 good/1 bad per function to at least all functionality is tested

        With limited functionality, a few tests per function felt reasonable
            Side note:     views broken down a lot to limited functionality. Carpentmentalize, easy to debug
            Refactored to meet this criteria and make testing easier

            NOTE: Did not test serializers and models. Odd thing and difficult to test (declaration vs functionality)

    Integration testing
        tests w/o MagicMock (aside from API calls)
        running several functions together rather than separate
        Could be done, will see depending on time

    Regression testing
        If we have time, not a priority

    system testing
        UI testing

        performance testing
            Huge user load
        
        security testing
            Just check for SQL injection, code injection

            Plans for Black Box testing, White Box testing (already doing with unit tests), Gray Box testing, IF WE HAD TIME

        accessibility testing
            devices - phones, laptop, computer

    acceptance testing
        Plan: In front of class as final


    


Testing Tools    
    MagicMock
    built-in Django & Django REST testing frameworks
    Unit tests (testing units)



Bug handling
    Prioritization
        Are there any bugs/possible bugs that we know of or could reasonably assume exist, and are we tackling them/not tackling them? Why?

    Stats for # of files, lines, and estimate how many bugs may be present
