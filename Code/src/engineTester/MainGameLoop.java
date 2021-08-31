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
		
		float[] vertices = {
				-0.5f, 0.5f, 0f,//v0
				-0.5f, -0.5f, 0f,//v1
				0.5f, -0.5f, 0f,//v2
				0.5f, 0.5f, 0f,//v3
		};
		
		int[] indices = {
				0,1,3,//top left triangle (v0, v1, v3)
				3,1,2//bottom right triangle (v3, v1, v2)
		};
		
		RawModel model = loader.loadtoVAO(vertices, indices);
				 
		 
		
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
