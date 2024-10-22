-- CreateTable
CREATE TABLE "RaceResult" (
    "id" SERIAL NOT NULL,
    "race_place" INTEGER NOT NULL,
    "bib_number" INTEGER NOT NULL,
    "full_name" TEXT NOT NULL,
    "gender" TEXT NOT NULL,
    "age" INTEGER NOT NULL,
    "city" TEXT NOT NULL,
    "state" TEXT NOT NULL,
    "chip_elapsed_time" TEXT NOT NULL,
    "gender_place" INTEGER NOT NULL,
    "age_group" TEXT NOT NULL,
    "age_place" INTEGER NOT NULL,
    "overall_pace" TEXT NOT NULL,
    "elapsed_time_minutes" DOUBLE PRECISION NOT NULL,
    "category" TEXT NOT NULL,

    CONSTRAINT "RaceResult_pkey" PRIMARY KEY ("id")
);
