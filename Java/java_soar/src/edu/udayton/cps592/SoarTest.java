package edu.udayton.cps592;

import sml.Kernel;
import sml.Agent;

public class SoarTest {
	
    public static void main(String[] args) {
        Kernel k = Kernel.CreateKernelInNewThread();
        Agent a = k.CreateAgent("soar");
        System.out.println(a.ExecuteCommandLine("echo Hello World"));
    }
    
}