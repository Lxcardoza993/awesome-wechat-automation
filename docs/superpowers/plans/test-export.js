export const meta = {
  name: "test-export",
  description: "Test that export works in workflow script.",
  phases: [{ title: "Test", detail: "Run a no-op agent" }]
};

phase("Test");
const result = await agent("Return the string hello", { label: "test", schema: { type: "object", properties: { value: { type: "string" } }, required: ["value"] } });
log(result.value);
