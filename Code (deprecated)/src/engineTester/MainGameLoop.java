package engineTester;

//OpenGL imports
import org.lwjgl.opengl.Display;

import models.RawModel;
import models.TexturedModel;
//import for rendering
import renderEngine.DisplayManager;
import renderEngine.Loader;
import renderEngine.Renderer;
import shaders.StaticShader;
import textures.ModelTexture;

//Project name
public class MainGameLoop {

	//Main method
	public static void main(String[] args) {
		
		//Create the display when the program runs
		DisplayManager.createDisplay();
		
		//Importing other classes
		Loader loader = new Loader();
		Renderer renderer = new Renderer();
		StaticShader shader = new StaticShader();
		
		float[] vertices = {
				-1.0f, 1.0f, 0f,//v0
				-1.0f, -1.0f, 0f,//v1
				0.5f, -0.5f, 0f,//v2
				0.5f, 0.5f, 0f,//v3
		};
		
		int[] indices = {
				0,1,3,//top left triangle (v0, v1, v3)
				3,1,2//bottom right triangle (v3, v1, v2)
		};
		
		float[] textureCoords = {
				0,0,
				0,1,
				1,1,
				1,0
		};
		
		RawModel model = loader.loadtoVAO(vertices, textureCoords, indices);
		ModelTexture texture = new ModelTexture(loader.loadTexture("image"));
		TexturedModel texturedModel = new TexturedModel(model, texture);
		
				 
		 
		
		//this while checks if CloseButtonPressed = Not
		//keeps the game running until CloseButtonPressed = True
		while(!Display.isCloseRequested()) {
			
			//game logic
			//rendering
			renderer.prepare();
			shader.start();
			renderer.render(texturedModel);
			shader.stop();
			DisplayManager.updateDisplay();
			
		}
		
		//Close the display once you end the while loop
		//And clean up the buffers
		shader.cleanUp();
		loader.CleanUp();
		DisplayManager.closeDisplay();

	}

}
