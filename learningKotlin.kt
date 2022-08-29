// package org.kotlinlang.play

interface defaultStudent {
    fun info() {}
}

abstract class Student(val name: String = "student") : defaultStudent {
    override info() {
        println("Hello")
    }
}

fun printMessage(vararg message: String): Unit {
    println("message with argument inside it")
    message.forEach { a -> println("Hello $a") }
}

class erson(val firstname: String, val lastname: String) {

    var nickName: String? = null
        set(value) {
            field = value
            println("nickname now set to $value")
        }
        get() = field

    init {
        println("init 1")
    }
    constructor() : this("peter", "parlet")
}

fun main() {
    val person = erson("Andrew", "Bate")

    println(person.firstname)
    person.nickName = "Ab"
    person.nickName = "braxk"
    println("=====\n \n===")
    println(person.nickName)
    println()

    val perso = erson()
    println(perso.firstname)

    println("Hello how are you doing, You must be good by now")
    printMessage("yes", "Boosh", "Subscribe")
}

// /**
//  * You can edit, run, and share this code.
//  * play.kotlinlang.org
//  */
// package org.kotlinlang.play
// fun printMessage(message: String = "BRUH, DEFAULT VALUE"): Unit{
//     println("message with argument inside it $message")
//     println(message)
// }
// val name: String? = "Bruh"
// fun funct() = "Hello Kotlin"

// var name:String? ="Richie"

// fun sayHello(who:String = "Richie"){
//     println("Hello Kotlin again bhai $who")
// }
// fun sayHello(greeting:String, vararg itemsToGreet:String){
//     itemsToGreet.forEach{a ->
// println("$greeting $a")
//     }

// }

// infix fun String.a(b:String):String{
//     return "$this and $b"
// }
// fun multiply(x: Int, y: Int) = x*y
// fun main(){
//     println("ana" a "buj")
//     var greetItems = listOf("Hi","Hello","Arigato")

//     sayHello("A","brandon","arthur","chloe")

//     val interestThings = mutableListOf("kotlin","mess","comics")
//     interestThings.forEachIndexed{indi,
//         it -> println("$it is at index $indi")
//     }

//     val map=mutableMapOf(1 to "a", 2 to "b")
//     map.put(4,"j")
//     map.forEach{ key, value -> println("$key -> $value")

//     }
//     var name: String ="Nate"
//     name="SOmething elsse"
//     printMessage()
//     println(multiply(3,5))
//     println("Hello how are you doing, You must be good by now")
//     printMessage("yes")
//     printMessage(name)

//     val interestThings = arrayOf("kotlin","mess","money")
//     val interestThings = arrayOf("kotlin","mess","comics", "books")
//     println(interestThings.size)
//     println(interestThings.get(0))
//     for (i in interestThings){
//         println("===")
//         println(i)
//     }

//     sayHello("Bootstrap")
//     sayHello()
//     println(funct())
//     val greetingToPrint = if(name != null) name else "Hi"
//     println("=======\n $name - $greetingToPrint \n==========")

//     if (name != null){
//         println("Excellent $name")
//     }else{
//         println("Excellent student")
//     }
//     when(name){
//         null -> println("Hi")
//         "richard" -> println("Hello $name")
//         "Richard" -> println("Well, hi big richard")
//         else -> println("You're not richard")
//     }
// }
