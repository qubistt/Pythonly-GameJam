package renderEngine;

//imports for OpenGL
import org.lwjgl.LWJGLException;
import org.lwjgl.opengl.ContextAttribs;
import org.lwjgl.opengl.Display;
import org.lwjgl.opengl.DisplayMode;
import org.lwjgl.opengl.GL11;
import org.lwjgl.opengl.PixelFormat;

//Project name
public class DisplayManager {
	
	//Integers for some basic args
	private static final int width = 1900;
	private static final int height = 1020;
	private static final int fps_cap = 60;
	
	//First method, run it to create a window
	public static void createDisplay() {
		
		//OpenGL version and compatibility settings
		ContextAttribs attribs = new ContextAttribs(3,2);
		attribs.withForwardCompatible(true);
		attribs.withProfileCore(true);
		
		//try and catch method tests code while execution
		//helpful for any errors
		try {
			//Simple code to create window with var dimensions
			//Attributes for OpenGL compatibility (line 21)
			Display.setDisplayMode(new DisplayMode(width, height));
			Display.create(new PixelFormat(), attribs);
			Display.setTitle("ADVWINDO");
		} catch (LWJGLException e) {
			e.printStackTrace();
		}
		
		//set OpenGL window size to match Java window size
		GL11.glViewport(0, 0, width, height);
	}
	
	//Second method to update display every frame, similar to Unity's
	public static void updateDisplay() {
		
		//Add an fps cap so comp doesn't overwork itself
		//Everything stays in order
		//Update the display according to the FPS
		Display.sync(fps_cap);
		Display.update();
	}
	
	//Third method, to simply close the display
	public static void closeDisplay () {
		
		Display.destroy();
		
	}

}
