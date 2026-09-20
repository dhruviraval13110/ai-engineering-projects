# Project Index

This file is the map for the portfolio.

## 01 — AI Expense Intelligence

Build a Python system that converts messy expense records into validated categories, summaries, and actionable analytics.

Core questions:
- How do we validate financial records?
- How do we handle unknown categories?
- How do we prevent duplicate transactions?
- How do we make the pipeline reproducible?

## 02 — E-Commerce Analytics Engine

Build an analytical system for orders, customers, products, and revenue.

Core questions:
- What is the right grain for each metric?
- How do joins change row counts?
- How do SQL window functions support business analysis?
- How do we validate analytical queries?

## 03 — Customer Churn Prediction

Build a supervised learning pipeline that predicts churn from structured customer data.

Core questions:
- What is the target?
- What information is available at prediction time?
- What is leakage?
- Which metric matches the decision cost?

## 04 — Recommendation System

Build a baseline recommendation engine using item similarity and user behavior.

Core questions:
- What makes a recommendation useful?
- How do we evaluate ranking systems?
- What happens with cold-start users?
- How do we separate offline metrics from product outcomes?

## 05 — Computer Vision Gesture System

Build a webcam-oriented gesture recognition pipeline.

Core questions:
- How do image frames become features?
- How do we smooth noisy predictions?
- How do we separate capture, inference, and presentation?

## 06 — NLP Document Classifier

Build a text classification pipeline.

Core questions:
- How should text be normalized?
- What does TF-IDF actually represent?
- How do we inspect false positives and false negatives?

## 07 — AI Data Analyst

Build a controlled system that helps users inspect datasets and generate structured analysis.

Core questions:
- How do we validate generated analysis?
- How do we prevent unsafe or irrelevant operations?
- How do we keep deterministic computations separate from natural-language explanation?

## 08 — RAG Knowledge Assistant

Build retrieval-augmented question answering over a local knowledge base.

Core questions:
- Why retrieval?
- What makes a chunk useful?
- How do we evaluate retrieval separately from generation?
- How do we reduce unsupported answers?

## 09 — Production ML API

Package a model or deterministic prediction pipeline behind an API.

Core questions:
- What belongs at the API boundary?
- How do we validate requests?
- How do we test failures?
- What should be logged?

## 10 — End-to-End AI Platform

Combine data ingestion, model/LLM components, APIs, evaluation, observability, and deployment design.

Core questions:
- Where should components communicate?
- What should be asynchronous?
- How do we version data, code, and models?
- How do we operate the system safely?
