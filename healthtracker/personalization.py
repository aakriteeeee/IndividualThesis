from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from django.contrib.auth import get_user_model
from .models import UserProfile

def train_personalization_model():
    # Fetch user profiles from the database
    user_profiles = UserProfile.objects.all()

    # Prepare data for the machine learning model
    data = []
    labels = []

    for profile in user_profiles:
        # Example: Assuming UserProfile has fields 'date_of_birth', 'bio', and 'profile_picture'
        data.append([profile.date_of_birth, profile.bio, profile.profile_picture])
        labels.append(profile.personalization_label)  # Personalization label based on user behavior

    # Convert categorical data to numerical format using Label Encoding
    le = LabelEncoder()
    
    data_encoded = le.fit_transform(data)
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data_encoded, labels, test_size=0.1, random_state=42)

    # X_train, X_test, y_train, y_test = train_test_split(data_encoded, labels, test_size=0.2, random_state=42)

    # Create and train the decision tree classifier
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # Evaluate the model on the test set
    accuracy = clf.score(X_test, y_test)
    print(f'Model Accuracy: {accuracy}')

    return clf

def get_personalized_recommendations(user):
    try:
        # Fetch user profile
        UserProfile = get_user_model()
        user_profile = UserProfile.objects.get(user=user)

        # Prepare user features for prediction
        user_data = [[user_profile.date_of_birth, user_profile.bio, user_profile.profile_picture]]
        le = LabelEncoder()
        user_data_encoded = le.transform(user_data)

        # Make personalized recommendation using the trained model
        personalized_label = clf.predict(user_data_encoded)[0]

        # Your logic to convert the personalized label to an actual recommendation
        recommendation = f'Your personalized recommendation based on label {personalized_label}'

        return recommendation
    except UserProfile.DoesNotExist:
        return "User profile does not exist"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Train the model when the module is imported
clf = train_personalization_model()
