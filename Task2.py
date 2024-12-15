import pandas as percival
import plotly.express as px

def load_dataset(file_path):
    try:
        data = percival.read_csv(file_path)
        data.columns = data.columns.str.strip()  
        print(f"Dataset loaded successfully. Columns: {list(data.columns)}")
        print(data.head())  
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def userVisualizationChoice():
    """Generate interactive visualizations based on user choice."""
    print("\nSelect a type of visualization:")
    print("1. Scatter Plot")
    print("2. Line Chart")
    print("3. Bar Chart")
    print("4. Histogram")
    print("5. Box Plot")



def generate_visualization(data):
    userVisualizationChoice()
    choice = input("Enter the number corresponding to your choice: ").strip()
    x_column = input("Enter the column for the X-axis: ").strip()
    y_column = input("Enter the column for the Y-axis (if applicable): ").strip()
    color_column = input("Enter the column for color grouping (optional, press Enter to skip): ").strip()

    try:
        if choice == '1':
            fig = px.scatter(data, x=x_column, y=y_column, color=color_column if color_column else None)
        elif choice == '2':
            fig = px.line(data, x=x_column, y=y_column, color=color_column if color_column else None)
        elif choice == '3':
            fig = px.bar(data, x=x_column, y=y_column, color=color_column if color_column else None)
        elif choice == '4':
            fig = px.histogram(data, x=x_column, color=color_column if color_column else None)
        elif choice == '5':
            fig = px.box(data, x=x_column, y=y_column, color=color_column if color_column else None)
        else:
            print("Invalid choice. Please try again.")
            return
        
        fig.show()
    except Exception as e:
        print(f"Error generating visualization: {e}")

def main():
    print("Welcome to the Interactive Visualization Tool")
    file_path = input("Enter the path to your CSV file: ").strip()
    data = load_dataset(file_path)
    
    if data is not None:
        while True:
            generate_visualization(data)
            again = input("\nDo you want to create another visualization? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Thank you for using the tool!")
                break

if __name__ == "__main__":
    main()

# Test case: make use of the CSV files folder 