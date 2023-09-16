/*
  Warnings:

  - Added the required column `inputTokens` to the `Message` table without a default value. This is not possible if the table is not empty.
  - Added the required column `outputTokens` to the `Message` table without a default value. This is not possible if the table is not empty.
  - Added the required column `totalCost` to the `Message` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Message" ADD COLUMN     "inputTokens" INTEGER NOT NULL,
ADD COLUMN     "outputTokens" INTEGER NOT NULL,
ADD COLUMN     "totalCost" DOUBLE PRECISION NOT NULL;
