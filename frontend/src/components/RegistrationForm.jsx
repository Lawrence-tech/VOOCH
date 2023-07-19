import React, { useState } from 'react';

const RegistrationForm = () => {
  const [imageFile, setImageFile] = useState(null);
  const [review, setReview] = useState('');

  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    setImageFile(file);
  };

  const handleReviewSubmit = (event) => {
    event.preventDefault();
    // Perform the review submission logic here
    // Use the imageFile and review states to send data to the backend
  };

  return (
    <form>
      <input type="file" accept="image/*" onChange={handleImageUpload} />
      <textarea value={review} onChange={(event) => setReview(event.target.value)}></textarea>
      <button type="submit" onClick={handleReviewSubmit}>Submit Review</button>
    </form>
  );
};

export default RegistrationForm;




// import React, { useState, useEffect } from 'react';

// const RegistrationForm = () => {
//   const [formData, setFormData] = useState({
//     username: '',
//     name: '',
//     email: '',
//     password: '',
//   });

//   const handleSubmit = (e) => {
//     e.preventDefault();

//     fetch('/register', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify(formData),
//     })
//       .then((response) => response.json())
//       .then((data) => {
//         // Handle the response as needed
//         console.log(data);
//       })
//       .catch((error) => {
//         // Handle any errors
//         console.error(error);
//       });
//   };

//   const handleChange = (e) => {
//     setFormData({
//       ...formData,
//       [e.target.name]: e.target.value,
//     });
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <input
//         type="text"
//         name="username"
//         value={formData.username}
//         onChange={handleChange}
//         placeholder="Username"
//       />
//       <input
//         type="text"
//         name="name"
//         value={formData.name}
//         onChange={handleChange}
//         placeholder="Name"
//       />
//       <input
//         type="email"
//         name="email"
//         value={formData.email}
//         onChange={handleChange}
//         placeholder="Email"
//       />
//       <input
//         type="password"
//         name="password"
//         value={formData.password}
//         onChange={handleChange}
//         placeholder="Password"
//       />
//       <button type="submit">Register</button>
//     </form>
//   );
// };

// export default RegistrationForm;
