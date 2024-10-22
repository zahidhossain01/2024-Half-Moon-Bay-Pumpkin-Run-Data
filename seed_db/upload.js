const fs = require('fs');
const csv = require('csv-parser');
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();

async function uploadCsvToDatabase() {
    const results = [];

    // Read the CSV file
    fs.createReadStream('../datasets/merged_5k-10k-halfm.csv')
        .pipe(csv())
        .on('data', (row) => {
            // Convert the row to the format you need for Prisma
            const raceResult = {
                race_place: parseInt(row.race_place),
                bib_number: parseInt(row.bib_number),
                full_name: row.full_name,
                gender: row.gender,
                age: parseInt(row.age),
                city: row.city,
                state: row.state,
                chip_elapsed_time: row.chip_elapsed_time,
                gender_place: parseInt(row.gender_place),
                age_group: row.age_group,
                age_place: parseInt(row.age_place),
                overall_pace: row.overall_pace,
                elapsed_time_minutes: parseFloat(row.elapsed_time_minutes),
                category: row.category
            };
            results.push(raceResult);
        })
        .on('end', async () => {
            try {
                // Insert all rows into the database
                for (const result of results) {
                    await prisma.raceResult.create({ data: result });
                }
                console.log('Data uploaded successfully!');
            } catch (error) {
                console.error('Error uploading data:', error);
            } finally {
                await prisma.$disconnect();
            }
        });
}

uploadCsvToDatabase();
