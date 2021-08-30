package engineTester;

//OpenGL imports
import org.lwjgl.opengl.Display;

//import for rendering
import renderEngine.DisplayManager;
import renderEngine.Loader;
import renderEngine.RawModel;
import renderEngine.Renderer;

//Project name
public class MainGameLoop {

	//Main method
	public static void main(String[] args) {
		
		//Create the display when the program runs
		DisplayManager.createDisplay();
		
		//Creating methods
		Loader loader = new Loader();
		Renderer renderer = new Renderer();
		
		//OpenGL vertices (must be counter-clockwise and triangle)
		 float[] vertices = {
				 	//bottom left
				    -0.5f, 0.5f, 0f,
				    -0.5f, -0.5f, 0f,
				    0.5f, -0.5f, 0f,
				    
				    //top right
				    0.5f, -0.5f, 0f,
				    0.5f, 0.5f, 0f,
				    -0.5f, 0.5f, 0f
				    
		 };
		 RawModel model = loader.loadtoVAO(vertices);
				 
		 
		
		//this while checks if CloseButtonPressed = Not
		//keeps the game running until CloseButtonPressed = True
		while(!Display.isCloseRequested()) {
			
			//game logic
			//rendering
			renderer.prepare();
			renderer.render(model);
			DisplayManager.updateDisplay();
			
		}
		
		//Close the display once you end the while loop
		//And clean up the buffers
		loader.CleanUp();
		DisplayManager.closeDisplay();

	}

}
