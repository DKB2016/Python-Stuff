import yaml
import jinja2

# Load YAML data
with open('C:\\Users\\david\\OneDrive\\Documents\\GitHub\\Python-Stuff\\jinja2\\switchconfig.yml', 'r') as file:
    data = yaml.safe_load(file)

# Load Jinja2 template
with open('C:\\Users\\david\\OneDrive\\Documents\\GitHub\\Python-Stuff\\jinja2\\switchconfig.jinja2', 'r') as file:
    template = jinja2.Template(file.read())

# Render the template with data from YAML
rendered_config = template.render(data)

# Output the rendered configuration
print(rendered_config)
