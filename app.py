from flask import Flask, request, jsonify
from DBconfig import connection

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    user_id = request.form.get('user_id')
    form_id = request.form.get('form_id')
    image_path = request.files['image']
    surname = request.form.get('surname')
    othernames = request.form.get('otherNames')
    sex = request.form.get('sex')
    dob = request.form.get('DoB'
    phone_number =
    whatsapp =
    email
    H_address =
    HF_zone =
    NoK =
    H_town =
    state =
    lga =
    nationality =
    tribe =
    other_lang =
    cls_town_mate =
    ctm_phone =
	 M_status =
    sep_div =
    bg =
    rhesus =
    profession =
    employed =
    occupation =
    pl_of_work =
    pos_at_work =
    pos_at_work_yr =
    student =
    course =
    school =
    pos_in_schl =
    pos_in_schl_yr =
    baptized =
    by_immerse =
    bap_denom =
    church_worker =
    unit_agency =
    church_grp =
    fel_grp =
    other_info =
    close_member =
    memship_date =
    chrch_status =
	 pos_held =
    pos_held_yr =
    office_use =


# Endpoint to handle image uploads
@app.route('/upload_image', methods=['POST'])
def upload_image():
    form_id = request.form.get('form_id')

    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({'error': 'No selected image'}), 400

    # Save the image with the form_id as the filename
    image_filename = f"{form_id}.jpg"
    image.save(image_filename)

    cursor = connection.cursor()
	
	try:
        # Get the user ID associated with the form_id
        cursor.execute("SELECT user_id FROM members_info WHERE form_id = %s", (form_id,))
        user_id = cursor.fetchone()[0]

        # Insert image information into the database, associating with the user
        cursor.execute("UPDATE members_info SET imagePath = %s WHERE user_id = %s",
                       (image_filename, user_id))

        # Commit the transaction
        connection.commit()
    except mysql.connector.Error as err:
        # Handle any database errors
        return jsonify({'error': f'Database error: {str(err)}'}), 500
    finally:
        # Close the database connection
        cursor.close()
        connection.close()

    return jsonify({'message': 'Image uploaded successfully', 'image_filename': image_filename}), 200


if __name__ == '__main__':
    app.run()
