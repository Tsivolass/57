import os
import json
import requests
import zipfile
import time
newbuds = [
            0,
            1,
            3,
            6,
            7,
            9,
            10,
            11
        ]
choices = ['bungalow', 'money', 'spawn', 'instantgrowth', 'autoplant']
seedlist = ['granddaddypurpleseed', 'sourdieselseed', 'greencrackseed', 'ogkushseed']

appdata_path = os.path.join(os.getenv('LOCALAPPDATA'), '..', 'LocalLow', 'TVGS', 'Schedule I Free Sample', 'saves')
print('Hello! This is a mod made by dev Tsivolass. If any bugs are found, DM me in discord (username is tsivolass) or send an email to devtsivolass@gmail.com \n If you wanna quit using my mod type exit at any point or press X on the top right of the terminal.  Thanks for using my mod :)')
choice = input('choices are: \n Bungalow\n spawn\n money\n instantgrowth\n autoplant ')
drugdata = ['OG', 'sour', 'green', 'purple']
if choice == 'exit':
    exit()
if choice in choices:
    gsave = int(input('Game save number: '))
    save_folder = os.path.join(appdata_path, f'SaveGame_{gsave}')  # Folder, not a file
    print(f"AppData Path: {appdata_path}")
    if os.path.isdir(save_folder):  # Use isdir() for folders
        print(f"Save folder found: {save_folder}")
    else:
        print("Save folder not found.")
        exit()
    
    if choice == 'autoplant':
        pchoice = input('choose a property with tents to instant grow: \n For bungalow, type Bungalow \n For motel, type Motel\n for sweatshop, type Sweatshop  ')
        schoice = input(f'type ogkushseed to plant OG kush in {pchoice} \n type sourdieselseed to plant Sour Diesels in {pchoice} \n type greencrackseed to plant Green Crack in {pchoice} \n type granddaddypurpleseed to plant Granddaddy Purple in {pchoice} \n')
        if pchoice == 'exit' or schoice == 'exit':
            exit()
        elif pchoice == 'bungalow' or pchoice == 'Bungalow':
            propertypath = os.path.join(save_folder, 'Properties', 'Bungalow', 'Objects')
    
            
            for foldername in os.listdir(propertypath):
                print('passed foldername')
    # Check if the folder starts with 'growtent_'
                if foldername.startswith('growtent_'):
                    print('passed growtent')
        # Construct the path to the Data.json file inside the folder
                    data_filepath = os.path.join(propertypath, foldername, 'Data.json')
        
        # Check if the Data.json file exists
                    if os.path.exists(data_filepath):
                        print('passed data filepath')
            # Open and read the Data.json file
                        try:
                            with open(data_filepath, 'r') as file:
                                data = json.load(file)
                                print('opened data filepath')
                        except json.JSONDecodeError as e:
                            print(e)
                        except IOError as e:
                            print(e)
                        data["SoilID"] = 'extralonglifesoil'
                        data["SoilLevel"] = 20.0
                        data["RemainingSoilUses"] = 2
                        print(f'Added soil to {data_filepath}')
                            
            # Modify the growthprogress value to 100.0
                        
                        print('passed soil addition')
                        plants = data["PlantData"]
                            
                                
                        plants["SeedID"] = schoice
                        plants["GrowthProgress"] = 1
                        plants["YieldLevel"] = 0.6700000166893005
                        plants["QualityLevel"] = 0.44999998807907107
                        plants["ActiveBuds"] = newbuds
                        print(f'Added {schoice} in {pchoice}')
                    
                        # Write the modified data back to the Data.json file
                        with open(data_filepath, 'w') as file:
                            json.dump(data, file, indent=4)
                            print('passed saving file')
                        print(f"Updated {data_filepath} with growthprogress set to 1.0")
                    else:
                        print(f"Data.json not found in {foldername}. Skipping...")
        elif pchoice == 'motel' or pchoice == 'Motel':
            propertypath = os.path.join(save_folder, 'Properties', 'Motel', 'Objects')
    
            
            for foldername in os.listdir(propertypath):
                print('passed foldername')
    # Check if the folder starts with 'growtent_'
                if foldername.startswith('growtent_'):
                    print('passed growtent')
        # Construct the path to the Data.json file inside the folder
                    data_filepath = os.path.join(propertypath, foldername, 'Data.json')
        
        # Check if the Data.json file exists
                    if os.path.exists(data_filepath):
                        print('passed data filepath')
            # Open and read the Data.json file
                        try:
                            with open(data_filepath, 'r') as file:
                                data = json.load(file)
                                print('opened data filepath')
                        except json.JSONDecodeError as e:
                            print(e)
                        except IOError as e:
                            print(e)
                        data["SoilID"] = 'extralonglifesoil'
                        data["SoilLevel"] = 20.0
                        data["RemainingSoilUses"] = 2
                        print(f'Added soil to {data_filepath}')
                            
            # Modify the growthprogress value to 100.0
                        
                        print('passed soil addition')
                        plants = data["PlantData"]
                            
                                
                        plants["SeedID"] = schoice
                        plants["GrowthProgress"] = 1
                        plants["YieldLevel"] = 0.6700000166893005
                        plants["QualityLevel"] = 0.44999998807907107
                        plants["ActiveBuds"] = newbuds
                        print(f'Added {schoice} in {pchoice}')
                    
                        # Write the modified data back to the Data.json file
                        with open(data_filepath, 'w') as file:
                            json.dump(data, file, indent=4)
                            print('passed saving file')
                        print(f"Updated {data_filepath} with growthprogress set to 1.0")
                    else:
                        print(f"Data.json not found in {foldername}. Skipping...")
        elif pchoice == 'sweatshop' or pchoice == 'Sweatshop':
            propertypath = os.path.join(save_folder, 'Properties', 'Sweatshop', 'Objects')
    
            
            for foldername in os.listdir(propertypath):
                print('passed foldername')
    # Check if the folder starts with 'growtent_'
                if foldername.startswith('growtent_'):
                    print('passed growtent')
        # Construct the path to the Data.json file inside the folder
                    data_filepath = os.path.join(propertypath, foldername, 'Data.json')
        
        # Check if the Data.json file exists
                    if os.path.exists(data_filepath):
                        print('passed data filepath')
            # Open and read the Data.json file
                        try:
                            with open(data_filepath, 'r') as file:
                                data = json.load(file)
                                print('opened data filepath')
                        except json.JSONDecodeError as e:
                            print(e)
                        except IOError as e:
                            print(e)
                        data["SoilID"] = 'extralonglifesoil'
                        data["SoilLevel"] = 20.0
                        data["RemainingSoilUses"] = 2
                        print(f'Added soil to {data_filepath}')
                            
            # Modify the growthprogress value to 100.0
                        
                        print('passed soil addition')
                        plants = data["PlantData"]
                            
                                
                        plants["SeedID"] = schoice
                        plants["GrowthProgress"] = 1
                        plants["YieldLevel"] = 0.6700000166893005
                        plants["QualityLevel"] = 0.44999998807907107
                        plants["ActiveBuds"] = newbuds
                        print(f'Added {schoice} in {pchoice}')
                    
                        # Write the modified data back to the Data.json file
                        with open(data_filepath, 'w') as file:
                            json.dump(data, file, indent=4)
                            print('passed saving file')
                        print(f"Updated {data_filepath} with growthprogress set to 1.0")
                    else:
                        print(f"Data.json not found in {foldername}. Skipping...")
    elif choice == 'bungalow':
        url = "https://www.dropbox.com/scl/fi/2p7blis6z7936l8o8knzv/Bungalow.zip?rlkey=4npl3yvxbd8d01fn78bqyn4u6&st=dkzfntat&dl=1"
        bungalowpath = os.path.join(save_folder, 'Properties')
        extract_path = os.path.join(bungalowpath, 'Bungalow')
        zip_path = os.path.join(bungalowpath, "Bungalow.zip")
        if not os.path.exists(extract_path):
            print(f"Creating Properties folder at: {extract_path}")
            os.makedirs(extract_path)

        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(zip_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"Download complete! File saved at: {zip_path}")

            # Extract the ZIP file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)  # Extracts into appdata_path
            print(f"Extraction complete! Files extracted to: {extract_path}")

            # Optional: Delete the ZIP file after extraction
            os.remove(zip_path)
            print("ZIP file deleted.")
        else:
            print(f"Failed to download. Status code: {response.status_code}")
    
    
    elif choice == 'money':
        moneypath = os.path.join(save_folder, 'Money.json')
        moneyvalue = int(input('Insert money to add (only number): '))

        # Function to update the OnlineBalance in the Money.json file
        def update_online_balance(file_path, amount):
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    data = json.load(file)

                if 'OnlineBalance' in data:
                    data['OnlineBalance'] += amount  # Add the moneyvalue to OnlineBalance
                    with open(file_path, 'w') as file:
                        json.dump(data, file, indent=4)
                    print(f"Updated OnlineBalance by {amount}. New balance: {data['OnlineBalance']}")
                else:
                    print(f"OnlineBalance field not found in {file_path}")
            else:
                print(f"File not found: {file_path}")

        # Update Money.json
        update_online_balance(moneypath, moneyvalue)
    
    elif choice == 'spawn':
        weedpath = os.path.join(save_folder, 'Players', 'Player_0', 'inventory.json')
        dchoice = input('Choose what to spawn in your inventory: \n 1. OG kush (type OG) \n 2. Sour diesels (type as sour) \n 3. green crack (type as green) \n 4. grandaddy purple (type as purple) \n 5. OG kush seeds (type OG_seeds) \n 6. Sour diesel seeds (type sour_seeds) \n 7. green crack seeds (type green_seeds) \n 8. grandaddy purple seeds (type purple_seeds) \n 9. Baseball Bat (type as bat) \n 10. Golden Skateboard (type as skateboard) ')
        if dchoice == 'exit':
            exit()
        elif os.path.exists(weedpath):
            with open(weedpath, 'r') as file:
                inventory_data = json.load(file)

            # Check if the choice is valid
            if dchoice not in ['OG', 'sour', 'green', 'purple', 'OG_seeds', 'sour_seeds', 'green_seeds', 'purple_seeds', 'bat', 'skateboard']:
                print("Invalid choice. No item spawned.")
                exit()

            # Find and remove one item with Quantity = 0 (excluding the last slot)
            slot_freed = False
            for index, item in enumerate(inventory_data['Items'][:-1]):  # Exclude the last slot
                item_data = json.loads(item)
                if item_data.get('Quantity', 1) == 0:  # Check if Quantity is 0
                    del inventory_data['Items'][index]  # Remove the item
                    slot_freed = True
                    print("Freed up one slot with Quantity = 0.")
                    break  # Exit after removing one item

            # If no slots were freed, exit
            if not slot_freed:
                print("No slots available (no items with Quantity = 0). Exiting.")
                exit()

            # Define the new item based on user choice
            if dchoice == 'OG':
                new_item = {
                    "DataType": "WeedData",
                    "DataVersion": 0,
                    "GameVersion": "0.2.9f4",
                    "ID": "ogkush",  # Ensure this matches the game's ID for OG kush
                    "Quantity": 20,   # Set the quantity as needed
                    "Quality": "Standard",
                    "PackagingID": "baggie"  # Set the packaging as needed
                }
            elif dchoice == 'sour':
                new_item = {
                    "DataType": "WeedData",
                    "DataVersion": 0,
                    "GameVersion": "0.2.9f4",
                    "ID": "sourdiesel",  # Ensure this matches the game's ID for Sour Diesels
                    "Quantity": 20,
                    "Quality": "Standard",
                    "PackagingID": "baggie"
                }
            elif dchoice == 'green':
                new_item = {
                    "DataType": "WeedData",
                    "DataVersion": 0,
                    "GameVersion": "0.2.9f4",
                    "ID": "greencrack",  # Ensure this matches the game's ID for Green Crack
                    "Quantity": 20,
                    "Quality": "Standard",
                    "PackagingID": "baggie"
                }
            elif dchoice == 'purple':
                new_item = {
                    "DataType": "WeedData",
                    "DataVersion": 0,
                    "GameVersion": "0.2.9f4",
                    "ID": "grandaddypurple",  # Ensure this matches the game's ID for Grandaddy Purple
                    "Quantity": 20,
                    "Quality": "Standard",
                    "PackagingID": "baggie"
                }
            elif dchoice == 'OG_seeds':
                new_item = {
                    "DataType": "ItemData",  # Seeds use "ItemData"
                    "DataVersion": 0,
                    "GameVersion": "0.2.9f4",
                    "ID": "ogkushseed",  # Ensure this matches the game's ID for OG kush seeds
                    "Quantity": 10,   # Set the quantity as needed
                }
            elif dchoice == 'sour_seeds':
                new_item = {
                    "DataType": "ItemData",
                    "DataVersion": 0,
                    "GameVersion": "0.2.9f4",
                    "ID": "sourdieselseed",  # Ensure this matches the game's ID for Sour Diesel seeds
                    "Quantity": 10,
                }
            elif dchoice == 'green_seeds':
                new_item = {
                    "DataType": "ItemData",
                    "DataVersion": 0,
                    "GameVersion": "0.2.9f4",
                    "ID": "greencrackseed",  # Ensure this matches the game's ID for Green Crack seeds
                    "Quantity": 10,
                }
            elif dchoice == 'purple_seeds':
                new_item = {
                    "DataType": "ItemData",
                    "DataVersion": 0,
                    "GameVersion": "0.2.9f4",
                    "ID": "granddaddypurpleseed",  # Ensure this matches the game's ID for Grandaddy Purple seeds
                    "Quantity": 10,
                }
            elif dchoice == 'bat':
                new_item = {
                    "DataType": "ItemData",
                    "DataVersion": 0,
                    "GameVersion": "0.2.9f4",
                    "ID": "baseballbat",  # Ensure this matches the game's ID for Grandaddy Purple seeds
                    "Quantity": 1,
                }
            elif dchoice == 'skateboard':
                new_item = {
                    "DataType": "ItemData",
                    "DataVersion": 0,
                    "GameVersion": "0.2.9f4",
                    "ID": "goldenskateboard",  # Ensure this matches the game's ID for Grandaddy Purple seeds
                    "Quantity": 1,
                }
            

            # Insert the new item into the freed-up slot
            inventory_data['Items'].insert(index, json.dumps(new_item))

            # Save the updated inventory back to the file
            with open(weedpath, 'w') as file:
                json.dump(inventory_data, file, indent=4)

            print(f"{dchoice} has been added to your inventory!")
        else:
            print(f"Inventory file not found: {weedpath}")
    elif choice == 'instantgrowth':
        pchoice = input('choose a property with tents to instant grow: \n For bungalow, type Bungalow \n For motel, type Motel\n for sweatshop, type Sweatshop  ')
        if pchoice == 'exit':
            exit()
        elif pchoice == 'bungalow' or pchoice == 'Bungalow':
            propertypath = os.path.join(save_folder, 'Properties', 'Bungalow', 'Objects')
    
        
            for foldername in os.listdir(propertypath):
    # Check if the folder starts with 'growtent_'
                if foldername.startswith('growtent_'):
        # Construct the path to the Data.json file inside the folder
                    data_filepath = os.path.join(propertypath, foldername, 'Data.json')
        
        # Check if the Data.json file exists
                    if os.path.exists(data_filepath):
            # Open and read the Data.json file
                        with open(data_filepath, 'r') as file:
                            data = json.load(file)
            
            # Modify the growthprogress value to 100.0
                        plants = data['PlantData']
                        if 'GrowthProgress' in plants and 'SeedID':
                            plants["GrowthProgress"] = 1
                            plants["YieldLevel"] = 0.6700000166893005
                            plants["QualityLevel"] = 0.44999998807907107
                            plants["ActiveBuds"] = newbuds
                           
                        else:
                            print(f"No 'growthprogress' key found in {data_filepath}. Skipping...")
                            continue

                        # Write the modified data back to the Data.json file
                        with open(data_filepath, 'w') as file:
                            json.dump(data, file, indent=4)

                        print(f"Updated {data_filepath} with growthprogress set to 1.0")
                    else:
                        print(f"Data.json not found in {foldername}. Skipping...")
        elif pchoice == 'motel' or pchoice == 'Motel':
            propertypath = os.path.join(save_folder, 'Properties', 'Motel Room', 'Objects')
    
        
            for foldername in os.listdir(propertypath):
    # Check if the folder starts with 'growtent_'
                if foldername.startswith('growtent_'):
        # Construct the path to the Data.json file inside the folder
                    data_filepath = os.path.join(propertypath, foldername, 'Data.json')
        
        # Check if the Data.json file exists
                    if os.path.exists(data_filepath):
            # Open and read the Data.json file
                        with open(data_filepath, 'r') as file:
                            data = json.load(file)
            
            # Modify the growthprogress value to 100.0
                        
                        plants = data['PlantData']
                        if 'GrowthProgress' in plants and 'SeedID':
                            plants["GrowthProgress"] = 1
                            plants["YieldLevel"] = 0.6700000166893005
                            plants["QualityLevel"] = 0.44999998807907107
                            plants["ActiveBuds"] = newbuds
                        else:
                            print(f"No 'growthprogress' key found in {data_filepath}. Skipping...")
                            continue

                        # Write the modified data back to the Data.json file
                        with open(data_filepath, 'w') as file:
                            json.dump(data, file, indent=4)

                        print(f"Updated {data_filepath} with growthprogress set to 100.0")
                    else:
                        print(f"Data.json not found in {foldername}. Skipping...")
        elif pchoice == 'sweatshop' or pchoice == 'Sweatshop':
            propertypath = os.path.join(save_folder, 'Properties', 'Sweatshop', 'Objects')
    
        
            for foldername in os.listdir(propertypath):
    # Check if the folder starts with 'growtent_'
                if foldername.startswith('growtent_'):
        # Construct the path to the Data.json file inside the folder
                    data_filepath = os.path.join(propertypath, foldername, 'Data.json')
        
        # Check if the Data.json file exists
                    if os.path.exists(data_filepath):
            # Open and read the Data.json file
                        with open(data_filepath, 'r') as file:
                            data = json.load(file)
            
            # Modify the growthprogress value to 100.0
                        plants = data['PlantData']
                        if 'GrowthProgress' in plants and plants['SeedID'] != '':
                            plants["GrowthProgress"] = 1
                            plants["YieldLevel"] = 0.6700000166893005
                            plants["QualityLevel"] = 0.44999998807907107
                            plants["ActiveBuds"] = newbuds
                        else:
                            print(f"No 'growthprogress' key found in {data_filepath}. Skipping...")
                            continue

                        # Write the modified data back to the Data.json file
                        with open(data_filepath, 'w') as file:
                            json.dump(data, file, indent=4)

                        print(f"Updated {data_filepath} with growthprogress set to 100.0")
                    else:
                        print(f"Data.json not found in {foldername}. Skipping...")
    elif choice == 'ron':
        print('Hey Ron! i figured you will find this easter egg by your scans or smh, so if you see this, i just wanna say thanks for everything :) ')
        print('also, my name is Dimitris (jim)')
        time.sleep(3)
else:
    print('Error: Invalid choice. Try running the script again!')