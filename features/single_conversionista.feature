Feature: Conversionistas title
    Scenario: can find search results
        When visit url "http://www.conversionista.com"
        
        Then title becomes "Konvertering – gör besökare till kunder | Conversionista! | Conversionista!"
