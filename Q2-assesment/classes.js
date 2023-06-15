//input -oral stories
//output -recorded oral stories and translated oral stories 
//process -create a class Oralstories
class Oralstories{
   constructor(length,morallessons,agegroup){
    this.morallessons=morallessons
    this.length=length
    this.agegroup=agegroup
   }
   story(){}
}
//5. Create a class called Product with attributes for name, price, and quantity.
//Implement a method to calculate the total value of the product (price * quantity).
//Create multiple objects of the Product class and calculate their total values.

//input name,price and quantity
//output calculation of total values
//process create a product class with methods for calculation

//2.input
//output
//ptocess create recipe class
//7. Create a FlightBooking class that represents a flight booking system. Implement
//methods to search for available flights based on destination and date, reserve
//seats for customers, manage passenger information, and generate booking
//confirmations.

//input-methods based on destination and date,reserve seats and passenger infomation
//output-available flights
//process-create a flightbooking class with methods to determine availbale flights
class FlightBooking{
    constructor(destination,seats,passengerInfo){
        this.seats=seats
        this.destination=destination
        this.passengerInfo=passengerInfo
    }
    searchAvailableFlight(){
        const seats=40
        const passengerInfo="all in"
        if(this.seats==seats && this.passengerInfo==passengerInfo){
            console.log("no flights available for booking")
        }
        else{
            console.log("flights are available for booking")
        }
    }
    }

