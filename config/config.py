import yaml

config = {
    "data_dir": {
        "crema_d":      "/peft-ser/CREMA-D/",
    },
    "project_dir":      "/peft-ser"
}

with open('config.yml', 'w') as outfile:
    yaml.dump(config, outfile, default_flow_style=False)