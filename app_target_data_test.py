#!flask/bin/python

import pprint

targets = [
    {
        'id': 1,
        'name': 'LPC546XX',
        'description': [
            {
                "ver": "Mbed OS 5.8",
                "name": "LPC546XX",
                "date": "May 2, 2018",
                "target_data" : { 'FLASH': 'N', 'RTC': 'Y', 'SPI': 'Y', 'I2C': 'Y', 'TRNG': 'N', 'SLEEP': 'Y'}
            },            
            {
                "ver": "Mbed OS 5.7",
                "name": "LPC546XX",
                "date": "May 2, 2018",
                "target_data" : { 'FLASH': 'N', 'RTC': 'N', 'SPI': 'N', 'I2C': 'Y', 'TRNG': 'N', 'SLEEP': 'Y'}
            }  
        ],                     
        'uri' : 'x'
    },
    {
        'id': 2,
        'name': 'LPC54114',
        'description': [
            {
                "ver": "Mbed OS 5.8",
                "name": "LPC54114",
                "date": "May 2, 2018",
                "target_data" : { 'FLASH': 'N', 'RTC': 'Y', 'SPI': 'N', 'I2C': 'Y', 'TRNG': 'N', 'SLEEP': 'Y'}
            },            
            {
                "ver": "Mbed OS 5.7",
                "name": "LPC54114",
                "date": "May 2, 2018",
                "target_data" : { 'FLASH': 'Y', 'RTC': 'Y', 'SPI': 'N', 'I2C': 'Y', 'TRNG': 'N', 'SLEEP': 'Y'}
            }  
        ],                     
        'uri' : 'x'
    },
]

def main():
    
    target = {
        'id': 3,
        'name': 'FF_LPC546XX',
        'description': [
            {
                "ver": "Mbed OS 5.8",
                "name": "LPC54114",
                "date": "May 2, 2018",
                "target_data" : { 'FLASH': 'N', 'RTC': 'Y', 'SPI': 'N', 'I2C': 'Y', 'TRNG': 'N', 'SLEEP': 'Y'}
            },            
            {
                "ver": "Mbed OS 5.7",
                "name": "LPC54114",
                "date": "May 2, 2018",
                "target_data" : { 'FLASH': 'Y', 'RTC': 'Y', 'SPI': 'N', 'I2C': 'Y', 'TRNG': 'N', 'SLEEP': 'Y'}
            }  
        ],                     
        'uri' : 'x'
    }

    pp = pprint.PrettyPrinter(indent=4)
    targets.append(target)
    
    pp.pprint(targets)
    
    new_description = {
            "ver": "Mbed OS 5.9",
            "name": "LPC54114",
            "date": "May 2, 2018",
            "target_data" : { 'FLASH': 'Y', 'RTC': 'Y', 'SPI': 'N', 'I2C': 'Y', 'TRNG': 'N', 'SLEEP': 'Y'}
        }  
    
    targets[0]['description'].append(new_description)

    pp.pprint(targets)
    

if __name__ == '__main__':
    main()
