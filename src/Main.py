from src.Path.Generator import Generator
from src.AlgorithmPicker import AlgorithmPicker

if __name__ == '__main__':
        generator = Generator()
        algo_picker = AlgorithmPicker()

        #executes algorithm on all of our generated 50 maps.

        for i in range(50):
            print("Executing forward on Map"+str(i))
            algo_picker.executeForwardAstar("resources/map"+str(i))
            print("Executing backwards on Map" + str(i))
            algo_picker.executeBackwardsAStar("resources/map"+str(i))
            print("Executing Adaptive on Map" + str(i))
            algo_picker.executeAdaptiveAStar("resources/map"+str(i))


        #debugging purpose ona smaller map
        # for i in range(50):
        #     generator = Generator()
        #    # generator.generateRandomMap(5,5,"test")
        #     algo_picker.executeBackwardsAStar("resources/map0")
        #     #algo_picker.executeBackwardsAStar("test")



