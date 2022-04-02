import java.util.Scanner;
public class melearnJava{
    public static void main(String[] args){
        System.out.println("Hello Duniya");
        Scanner sc = new Scanner(System.in);
        int a = 4;
        int b = 5;
        System.out.println("Hello Duniya, you've chosen "+ (a+b) + " " + (a*b) +" as your partner");

        int mearray[] = new int[20];


        if(a==4){
            System.out.println("a is 4");
        }else if (a==5){
            System,out.println("a is 5");
        }else{
            System.out.println("He's not in our league bruhhh.")
        }
        while(b>0){
            print("bol bhai");
            b++
        }
        for(int fooFor = 0; fooFor < 10; fooFor++){
            System.out.println("fooFor @ " + ;fooFor);
        }

        int month =3
        String monthString
        switch(month){
            case 1: monthString = "January";
            break;
            case 2: monthString = "February";
            break;
            default: monthString = "March";
            break;
        }

        Sytem.out.println("This is the turn for classes and functions");
        class Bicycle{
            public int cab;
            //default constructor
            public Bicycle(){
                cab=90;
            }
            //constructor with arguments
            public Bicycle(int cab){
                this.cab=cab;
            }

            //method
            public int getCab(){
                return cab;
            }
        }

        class PennyFarthing extends Bicycle{
            public PennyFarthing(int str){
                super(str);
            }
            @Override
            publiv void setGear(int gear){
                this.gear=0;
            }

            //Holy grail coming up 
            // Interfacess //

            public interface Edible{
                public void eat();
            }
            public interface Digestible{
                public void digest();
                public default void defaultMethod(){
                    System.out.println("Hi, from the default method....");
                }
            }

            public class Fruit implements Edible, Digestible{
                @Override
                public void eat(){
                    //....
                }
            }


            public class ExampleClass extends ExampleClassParet implements InterfaceOne, Interfacetwo{
                
            }






        }
    }
}