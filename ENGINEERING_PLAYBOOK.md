# Engineering Playbook

## 1. Start with the decision

Do not begin with a model. Begin with the decision the system supports.

## 2. Establish a baseline

A simple baseline gives you a reference point. Without it, a more complex model can look impressive while adding little value.

## 3. Protect the evaluation

The test set is evidence. Do not repeatedly optimize against it and then pretend it is unseen.

## 4. Separate concerns

Keep ingestion, transformation, inference, evaluation, and presentation separate.

## 5. Make failure visible

Errors should be observable and actionable. Silent corruption is worse than an explicit failure.

## 6. Test behavior

A test should express a property that must remain true.

## 7. Document trade-offs

For every meaningful technical decision, record:
- context;
- options considered;
- chosen approach;
- reason;
- consequence.

## 8. Security

Never commit:
- API keys;
- passwords;
- private datasets;
- access tokens;
- credentials.

Use environment variables and secret managers where appropriate.

## 9. Performance

Measure before optimizing. Identify the actual bottleneck.

## 10. Deployment

Deployment is not the final command. It includes:
- configuration;
- observability;
- failure handling;
- rollback;
- dependency management;
- versioning.

## 11. Interview rule

If a project is on the resume, be prepared to explain:
- architecture;
- data;
- algorithm;
- metrics;
- failures;
- trade-offs;
- testing;
- deployment;
- what you would change next.
