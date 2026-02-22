-- Create Database
CREATE DATABASE IF NOT EXISTS art_gallery;
USE art_gallery;

-- Create Table
CREATE TABLE IF NOT EXISTS imagedetails (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Path VARCHAR(255) NOT NULL,
    Exif TEXT NOT NULL,
    Colors TEXT NOT NULL
);

-- Insert Sample Data
INSERT INTO imagedetails (Title, Path, Exif, Colors) VALUES 
('Sunset at the Pier', 'sunset.jpg', '{"camera": "Canon EOS 5D", "lens": "24-70mm f/2.8", "focal_length": "50mm"}', '["#FF5733", "#C70039", "#900C3F"]'),
('Mountain Morning', 'mountain.jpg', '{"camera": "Nikon D850", "lens": "70-200mm f/2.8", "focal_length": "100mm"}', '["#2E86C1", "#AED6F1", "#1B4F72"]'),
('City Lights', 'city.jpg', '{"camera": "Sony A7III", "lens": "35mm f/1.4", "focal_length": "35mm"}', '["#F1C40F", "#2C3E50", "#E74C3C"]'),
('Forest Path', 'forest.jpg', '{"camera": "Fujifilm X-T4", "lens": "16-55mm f/2.8", "focal_length": "24mm"}', '["#229954", "#196F3D", "#D4AC0D"]'),
('Abstract Waves', 'waves.jpg', '{"camera": "Olympus OM-D", "lens": "12-40mm f/2.8", "focal_length": "12mm"}', '["#8E44AD", "#A569BD", "#2980B9"]');
