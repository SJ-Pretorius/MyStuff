using System;

public class Light
{
    public string Type;
    public int Watts;
    public int Lumens;
    public int Status;

    public Light(string type, int watts, int lumens)
    {
        Type = type;
        Watts = watts;
        Lumens = lumens;
        Status = 0;
    }

    public void On()
    {
        Console.WriteLine("Light is on!");
        Status = 1;
    }

    public void Off()
    {
        Console.WriteLine("Light is off!");
        Status = 0;
    }
}

public class Program
{
    public static void Main()
    {
        Light newLight = new Light("led", 5, 250);

        Console.WriteLine(newLight.Lumens);
        newLight.On();
        Console.WriteLine(newLight.Status);
    }
}
