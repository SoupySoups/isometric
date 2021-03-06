## Welcome to the Documentation

## Modules
### External Modules
 - The [isometric game](https://github.com/SoupySoups/isometric) uses a uses [Pygame](https://www.pygame.org) to manage and draw to a window.
 - We also use [PyTMX](https://github.com/bitcraft/pytmx) to parse and load levels, tilesets, and properties into the application.

### Internal Modules 
  - The game primarily runs through the application manager, located at `src/managers/application_manager.py` to load all other internal modules/ managers.

## Creating levels
### Software
 - For our level creation software we use [Tiled](https://www.mapeditor.org/) it is a very flexible 2D map editor and is highly recommended to install if you are going to develop new levels.

### Creating a new tileset
 - When creating a new level, you need a couple of prerequisites. Before creating a map you must have a tile set to pull all the images from. You can either use one of the pre-made tilesets (skip the rest of this section) or create your own.

 1.  Open your favorite image editor and create your tile art, each tile should be 20x24 but the overall image size does not matter as long as each tile is on the 20x24 grid starting at `(0, 0)`.
![grid](/isometric/assets/grid.png)

 2.  Start by opening and going to File > New > New Tileset
 3.  Name your tileset a **meaningful** name and set your source to your previously created image.
 4.  Hit save as and save in a spot you can remember as a `.tsx` file.

### Creating a new map
 1. Go to File > New > New Map
 2. In the options panel that appears, make sure the following properties are set appropriately:
 - `Orientation` is set to `Isometric`
 - `Tile layer format` is set to `CSV`
 - `Tile render order` is set to `Right Down`
 - Tile size `Width` is set to `20`
 - Tile size `Height` is set to `10`
 - `Fixed` box is `checked`
 3. Under Map size set your desired levels `Width` and `Height` and hit `OK`.

### Legal names
Components should only be named any of the following names.
 - logging
 - configuration
 - window
 - screen
 - level
 - object
 - component
 - render

Naming different names may result in undesired behavior

### Adding components
This game uses a entity component system or ECS for short, this means that each entity does not get its own file but rather each entity gets components added to it to control certain behaviors.

To add a property you can select any object you have placed down, go to its properties panel, and add a new property by pressing the blue `+` in the bottom left corner. Name this new property `component_someComponent` and set its type to string. In this new field set its value to something like `path.to.your.component` such as `src.components.someComponent`. Now in python if you add a file at `/src/components/someComponent.py` and create this basic component:
```py
from basic_component import template

class component(template):
    def __init__(self, args) -> None:
        super().__init__(args)
        # Program your component here.
        print(self.arguments)
```


As you can see here we are creating a basic message property for our component, but how do we pass this `"message"` argument?

## Adding component arguments
To pass an argument to a component simply create another property in tiled with your desired argument type and name it `nameOfYourComponent.argumentName` such as `someComponent.message`. Set this fields value to your data such as `"Hello World"` and now that argument will be passed to your component in the `args` dictionary!
![components](/isometric/assets/components.png)

### Argument to self references
The component system also supports attribute referencing. Lets say you need to pass the the x position set by tiled to a component as an argument. You could manually copy each x position in tiled to a argument but that would be tedious. Instead you can use the `attribute` descriptor. To use this simply set your attribute value to, in our example, `attribute.self.x`, and when the object is loaded will be parsed into the real x value of the object.

### Argument to component references
You can also reference and sync attributes to other component attributes by using this format `attribute.otherComponent.valueName` in attribute fields.
